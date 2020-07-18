from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.


def rooms(request):
    return render(request, 'chat/rooms.html')


def room(request, room_name):
    return render(request, 'chat/chatroom.html', {'room_name': room_name})
