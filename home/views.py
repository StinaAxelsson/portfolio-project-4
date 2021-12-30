from django.shortcuts import render
from django.views import View
from .models import Post


class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')

        context = {
            'home': posts,
            
        }

        return render(request, 'home.html', context)
