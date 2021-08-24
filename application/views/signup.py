from django.views.generic import CreateView
from django.urls import reverse_lazy
from ..forms import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')  # reverseをクラスベースビューのクラス変数として書くときに利用。reverse は urls.py がまだ動いていないので解決できない
    template_name = 'registration/signup.html'