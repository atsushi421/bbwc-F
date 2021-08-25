from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from ..models import *


class RoomListView(View):
    def get(self, request, *args, **kwargs):
        room_list = Room.objects.all()
        
        context = {
            'room_list' : room_list,
        }
        return render(request, 'chat/room_list.html', context)
    
    
    def post(self, request, *args, **kwargs):
        name = request.POST['room_name']
        room = Room.objects.create(name=name)

        
        return redirect('/chat/' + name, args=[name])
        
        