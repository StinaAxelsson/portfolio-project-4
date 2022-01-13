from django.shortcuts import render
from django.views import View


class Messages(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'private_message.html')
