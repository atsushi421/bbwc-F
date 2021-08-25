from django.views.generic import UpdateView
from django.urls import reverse_lazy
from ..models import User


class ProfileEditView(UpdateView):
    model = User
    fields = ('key1', 'key2', 'key3', 'key4', 'key5')
    template_name = 'registration/profile_edit.html'
    success_url = reverse_lazy('index')