from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.conf import settings

# メール認証をするときのテンプレ
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


User = get_user_model()  # ユーザモデルはこの方法で取ってくるのが正式。変更したいときのため

subject = '登録確認'  # メールのタイトル
# メールの本文
message_template = """
ご登録ありがとうございます。
以下URLをクリックして登録を完了してください。

"""

# URL を組み立てて返す
def get_activate_url(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    return settings.FRONTEND_URL + "/activate/{}/{}/".format(uid, token)  # ユーザはこの URL をクリックすると、認証完了


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        # commit=Falseだと、DBに保存されない
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
            
        # 確認するまでログイン不可にする
        user.is_active = False
            
        if commit:
            user.save()
            activate_url = get_activate_url(user)  # URL を生成
            message = message_template + activate_url  # メール本文に URL を付ける
            user.email_user(subject, message)  # メール送信
        return user
        
        
# ユーザ認証を行い、ユーザを有効化して、DBに保存する
def activate_user(uidb64, token):    
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except Exception:
        return False

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return True
            
    return False

