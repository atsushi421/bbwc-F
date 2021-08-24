from django.views import View
from django.shortcuts import render
from ..models import *


class FileListView(View):
    def get(self, request, *args, **kwargs):
        room_name = kwargs['room_name']
        room = Room.objects.get(name=room_name)
        file_list = File.objects.filter(room=room)
        
        context = {
            'room':room,
            'file_list' : file_list,
        }
        return render(request, 'chat/file_list.html', context)