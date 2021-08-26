from django.views import View
from django.shortcuts import render
from ..forms import UploadForm
from ..models import *

class ChatView(View):
    def get(self, request, *args, **kwargs):
        room_name = kwargs['room_name']
        user = User.objects.get(id=request.user.id)
        messages = Message.objects.filter(room__name=room_name).order_by('-created_at')[:50]
        room = Room.objects.filter(name=room_name)[0]
        form = UploadForm()
        num_bookmark = room.user_set.count()
        num_jourclub = room.jourclub.count()
        
        context = {
            'messages': messages,
            'room': room,
            'form':form,
            'num_bookmark':num_bookmark,
            'num_jourclub':num_jourclub
        }
        
        if(room in user.book.all()):
            context |= {'book_flag':True}
        
        if(room in user.jourclub.all()):
            context |= {'jourclub_flag':True}
            
        # 輪講希望を出している部屋に輪講希望者が2人以上いれば、通知を表示
        jourclub_rooms = user.jourclub.all()
        for jourclub_room in jourclub_rooms:
            if(jourclub_room.jourclub.count() >= 2):
                context |= {'chance_flag': True }
                break
        
        
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
        
        elif('rm_bookmark' in request.POST):
            user.book.remove(room)
            user.save()
            message =  "この部屋のブックマークを消しました"
        
        elif('jourclub' in request.POST):  # 輪講希望の場合
            user.jourclub.add(room)
            user.save()
            message =  "輪講希望を出しました"
        
        elif('rm_jourclub' in request.POST):
            user.jourclub.remove(room)
            user.save()
            message =  "輪講希望を取り下げました"
        
        elif('start_journal_club' in request.POST):
            Paper.objects.create(name=room_name, user=user)
            user.score += 20
            user.save()
            message =  "輪講を開始します。\nミーティングのリンクを貼り、ミーティングに参加してください。"
        
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
        num_bookmark = room.user_set.count()
        num_jourclub = room.jourclub.count()
        
        context = {
            'messages': messages,
            'room': room,
            'form':form,
            'num_bookmark':num_bookmark,
            'num_jourclub':num_jourclub
        }
        
        if(room in user.book.all()):
            context |= {'book_flag':True}
        
        if(room in user.jourclub.all()):
            context |= {'jourclub_flag':True}
            
        # 輪講希望を出している部屋に輪講希望者が2人以上いれば、通知を表示
        jourclub_rooms = user.jourclub.all()
        for jourclub_room in jourclub_rooms:
            if(jourclub_room.jourclub.count() >= 2):
                context |= {'chance_flag': True }
                break
        
        return render(request, 'chat/chat_room.html', context)