from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# chat/views.py
from django.shortcuts import render

@login_required
def index(request):
    return render(request, 'chat/index.html', {})

@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })