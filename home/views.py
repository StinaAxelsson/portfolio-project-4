from django.shortcuts import render
from django.views import View
from .models import Post
from .form import PostUpload


class PostListView(View):

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostUpload()

        context = {
            'home': posts,
            'form': form,
            
        }

        return render(request, 'home.html', context)
