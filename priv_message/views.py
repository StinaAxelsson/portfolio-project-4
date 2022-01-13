from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from .models import PrivateMessage
from socialnetwork.models import Users

class PM_detail(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        message = Users.objects.get(pk=pk)
        form = CommentForm()
        messages = PrivateMessage.objects.filter(message=message).order_by('-created_on')

        context = {
            'message':message,
            'form': form,
            'messages': messages,
        }
        return render(request, 'direct_message.html', context)