from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Inbox
from django.contrib.auth.models import User




class Messages(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'private_message.html')


def Threads(request, *args, **kwargs):
    
    messages = Inbox.get_message(user=request.user)
    is_thread = None
    threads = None

    if messages:
        message = messages[0]
        is_thread = message['user'].username
        threads = Inbox.objects.filter(user=request.user, receiver=message['user'])
        threads.update(read=True)

        for message in messages:
            if message['user'].username == is_thread:
                message['unread'] = 0

    context = {
        'threads': threads,
        'messages': messages,
        'is_thread': is_thread,
    }
    

    return render(request, 'private_message.html', context)