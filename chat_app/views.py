import json

from django.shortcuts import render
from django.http import JsonResponse
from .models import Chat



# Create your views here.
def chat_view(request):
    if request.method == "GET":
        chats = Chat.objects.all()
        data = list(chats.values())
        return JsonResponse(data, safe=False)

    def chat_view(request):
    if request.method == "GET":
        chats = Chat.objects.all()
        data = list(chats.values())
        return JsonResponse(data, safe=False)

    if request.method == "POST":
          data = json.loads(request.body)