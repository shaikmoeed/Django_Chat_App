from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'chat/index.html', {})

@login_required
def room(request, room_name):
    print(request.user.username)
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': serializers.serialize('json', [request.user,]),
    })
