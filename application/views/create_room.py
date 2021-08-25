from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from ..models import *


class CreateRoomView(View):
    def get(self, request, *args, **kwargs):
        context = {
        }
        
        return render(request, 'chat/create_room.html', context)
    
    
    def post(self, request, *args, **kwargs):
        name = request.POST['room_name']
        room = Room.objects.create(name=name)

        
        return redirect('/chat/' + name, args=[name])