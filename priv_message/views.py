from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Inbox, Thread
from .forms import InboxForm, MessageForm


class InboxList(View):
    def get(self, request, *args, **kwargs):
        inboxthread = Inbox.objects.filter(
            Q(user=request.user) | Q(user_receiver=request.user)
        )
        context = {
            'inboxthread': inboxthread,
        }
        return render(request, 'private_message.html', context)

class CreateInboxForm(View):
    def get(self, request, *args, **kwargs):
        form = InboxForm()

        context = {
            'form': form
        }

        return render(request, 'private_message.html', context)

    def post(self, request, *args, **kwargs):
        form = InboxForm(request.POST)

        username = request.POST.get('username')

        try:
            user_receiver = User.objects.get(username=username)
            if Inbox.objects.filter(
                user=request.user, user_receiver=receiver).exists():
                inboxthread = Inbox.objects.filter(user=request.user, user_receiver=receiver)[0]
                return redirect('inbox', pk=inboxthread.pk)
                       
            elif Inbox.objects.filter(
                user=receiver, user_receiver=request.user).exists():
                inboxthread = Inbox.objects.filter(user=receiver, user_receiver=request.user)[0]
                return redirect('inbox', pk=inboxthread.pk)

            if form.is_valid():
                inboxthread = Inbox(user=request.user,user_receiver=receiver)
                inboxthread.save()
                return redirect('inbox', pk=inboxthread.pk)
        except:
            return redirect('priv-message')


class Message(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        inbox = Inbox.objects.get(pk=pk)
        message_thread = Thread.objects.filter(inbox__pk__contains=pk)

        context ={
            'inbox': inbox,
            'form': form,
            'message_thread': message_thread
        }
        return render(request, 'private_message.html', context)

class CreateMessage(View):
    def post(self, request, pk, *args, **kwargs):
        inbox = Inbox.objects.get(pk=pk)
        if inbox.user_receiver == request.user:
            user_receiver = inbox.user
        else:
            user_receiver = inbox.user_receiver
        
        message = Thread(
            thread=thread,
            sender = request.user,
            receiver = receiver,
            body=request.POST.get('message')
        )

        message.save()
        return redirect('thread', pk=pk)