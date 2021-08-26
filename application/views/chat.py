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
            
        # 輪講希望者が2人以上いれば
        if(room.jourclub.count() >= 2):
            context |= {'chance_flag': True }
        
        
        return render(request, 'chat/chat_room.html', context)
    
    def post(self, request, *args, **kwargs):
        room_name = kwargs['room_name']
        room = Room.objects.get(name=room_name)
        user = User.objects.get(id=request.user.id)
        form = UploadForm(request.POST, request.FILES)
        
        if('bookmark' in request.POST):  # ブックマークの場合
            user.book.add(room)
            user.save()
            message =  "I've bookmarked this room."
        
        elif('rm_bookmark' in request.POST):
            user.book.remove(room)
            user.save()
            message =  "I've deleted my bookmarks for this room."
        
        elif('jourclub' in request.POST):  # 輪講希望の場合
            user.jourclub.add(room)
            user.save()
            message =  "I've requested to do the journal club."
        
        elif('rm_jourclub' in request.POST):
            user.jourclub.remove(room)
            user.save()
            message =  "I've withdrawn my request to do the journal club."
        
        elif('start_journal_club' in request.POST):
            if(Paper.objects.filter(name=room_name).count() == 0):
                paper_instance = Paper.objects.create(name=room_name)
                user.paper_set.add(paper_instance)
                
            else:
                paper_instance = Paper.objects.get(name=room_name)
                user.paper_set.add(paper_instance)
            
            user.jourclub.remove(room)
            user.score += 20
            user.save()
            message =  "Start the journal club.\nPlease paste the meeting link and join the meeting."
        
        elif('upload' in request.POST):  # ファイルアップロードの場合
            file = request.FILES['file']
            if form.is_valid():
                file_instance = File(file=file, room=room, user=user)
                file_instance.save()
                user.score += 10
                user.save()
                
            message = file.name + " has been uploaded."
            
        else:
            message = request.POST['message']
            
        user = User.objects.get(id=request.user.id)
        Message.objects.create(room=room, user=user, content=message)
        
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
            
        # 輪講希望者が2人以上いれば
        if(room.jourclub.count() >= 2):
            context |= {'chance_flag': True }
        
        return render(request, 'chat/chat_room.html', context)