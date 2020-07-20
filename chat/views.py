from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/login/')
def rooms(request):
    return render(request, 'chat/rooms.html')


@login_required(login_url='/login/')
def room(request, room_name):
    return render(request, 'chat/chatroom.html', {'room_name': room_name})
