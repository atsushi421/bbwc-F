from django.views.generic import UpdateView
from django.urls import reverse_lazy
from ..models import User


class ProfileEditView(UpdateView):
    model = User
    fields = ('keyword1', 'keyword2', 'keyword3', 'keyword4', 'keyword5')
    template_name = 'registration/profile_edit.html'
    success_url = reverse_lazy('index')