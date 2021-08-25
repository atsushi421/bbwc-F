from django.views import View
from django.shortcuts import render
from ..forms import UploadForm
from ..models import *

class ChatView(View):
    def get(self, request, *args, **kwargs):
        room_name = kwargs['room_name']
        
        messages = Message.objects.filter(room__name=room_name).order_by('-created_at')[:50]
        room = Room.objects.filter(name=room_name)[0]
        form = UploadForm()
        
        context = {
            'messages': messages,
            'room': room,
            'form':form
        }
        
        return render(request, 'chat/chat_room.html', context)
    
    def post(self, request, *args, **kwargs):
        room_name = kwargs['room_name']
        room = Room.objects.get(name=room_name)
        user = User.objects.get(id=request.user.id)
        form = UploadForm(request.POST, request.FILES)
        
        if('bookmark' in request.POST):  # ブックマークの場合
            user.book.add(room)
            user.save()
            message =  "この部屋をブックマークしました"
        
        elif('upload' in request.POST):  # ファイルアップロードの場合
            file = request.FILES['file']
            if form.is_valid():
                file_instance = File(file=file, room=room, user=user)
                file_instance.save()
                user.score += 10
                user.save()
                
            message = file.name + " をアップロードしました"
            
        else:
            message = request.POST['message']
            
        user_name = request.user.username
        Message.objects.create(room=room, name=user_name, content=message)
        
        messages = Message.objects.filter(room__name=room_name).order_by('-created_at')[:50]
        room = Room.objects.filter(name=room_name)[0]
        
        
        context = {
            'messages': messages,
            'room': room,
            'form':form
        }
        
        return render(request, 'chat/chat_room.html', context)