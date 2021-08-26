from django.views import View
from django.shortcuts import render
from ..models import *


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        score = user.score
        file_list = File.objects.filter(user_id=request.user.id)
        paper_list = Paper.objects.filter(user_id=request.user.id)
        
        context = {
            'score':score,
            'file_list' : file_list,
            'paper_list' : paper_list
        }
        return render(request, 'registration/profile.html', context)