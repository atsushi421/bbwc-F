from django.contrib import admin
from django.urls import path, include  # include は委譲
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import signup, activate, index



urlpatterns = [
    path('', login_required(index.IndexView.as_view()), name='index'),  # トップページをログイン必須とする
    path('', include('django.contrib.auth.urls')),  # ログイン関係で、django がもともと用意している URL とマッチした場合表示。login, logout などのURLが含まれている
    path('signup/', signup.SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', activate.ActivateView.as_view(), name='activate'),  # <>はビュー側でパラメータとして受け取れる
]