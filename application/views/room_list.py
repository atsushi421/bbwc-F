from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from ..models import *


class RoomListView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'chat/room_list.html', context)
    
    
    def post(self, request, *args, **kwargs):
        name = request.POST['room_name']
        Room.objects.create(name=name)
        
        return redirect(reverse('chat_room', args=[name]))
        
        