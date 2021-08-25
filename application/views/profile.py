from django.views import View
from django.shortcuts import render
from ..models import *


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        score = File.objects.filter(user_id=request.user.id).count() * 10
        file_list = File.objects.filter(user_id=request.user.id)
        
        context = {
            'score':score,
            'file_list' : file_list,
        }
        return render(request, 'registration/profile.html', context)