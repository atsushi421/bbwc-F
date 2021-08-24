from django.views import View
from django.shortcuts import render
from ..models import *

class ChatView(View):
    def get(self, request, *args, **kwargs):
        room_name = kwargs['room_name']
        
        messages = Message.objects.filter(room__name=room_name).order_by('-created_at')[:50]
        room = Room.objects.filter(name=room_name)[0]
        
        context = {
            'messages': messages,
            'room': room
        }
        
        return render(request, 'chat/chat_room.html', context)
    
    def post(self, request, *args, **kwargs):
        message = request.POST['message']
        user_name = request.user.username
        room_name = kwargs['room_name']
        room = Room.objects.get(name=room_name)
        Message.objects.create(room=room, name=user_name, content=message)
        
        messages = Message.objects.filter(room__name=room_name).order_by('-created_at')[:50]
        room = Room.objects.filter(name=room_name)[0]
        
        context = {
            'messages': messages,
            'room': room
        }
        
        return render(request, 'chat/chat_room.html', context)