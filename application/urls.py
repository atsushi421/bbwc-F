from django.contrib import admin
from django.urls import path, include  # include は委譲
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import signup, activate, index, chat, room_list, profile, file_list
from django.conf.urls.static import static
from config_dir import settings



urlpatterns = [
    path('', login_required(index.IndexView.as_view()), name='index'),  # トップページをログイン必須とする
    path('', include('django.contrib.auth.urls')),  # ログイン関係で、django がもともと用意している URL とマッチした場合表示。login, logout などのURLが含まれている
    path('signup/', signup.SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>', profile.ProfileView.as_view(), name='profile'),
    path('activate/<uidb64>/<token>/', activate.ActivateView.as_view(), name='activate'),  # <>はビュー側でパラメータとして受け取れる
    path('chat/<str:room_name>', chat.ChatView.as_view(), name='chat_room'),
    path('room_list/', room_list.RoomListView.as_view(), name='room_list'),
    path('file_list/<str:room_name>', file_list.FileListView.as_view(), name='file_list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)