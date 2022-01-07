from django.shortcuts import render
from django.views import View
from .models import Post
from .forms import PostForm, CommentForm
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


"""
Views for the feed, listing all existing posts that been created,
and a form to create new posts for the feed.
"""
class PostList(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()

        context = {
            'post_feed': posts,
            'form': form,
        }

        return render(request, 'post_feed.html', context)


    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        context = {
            'post_feed': posts,
            'form': form,
        }

        return render(request, 'post_feed.html', context)


"""
Views for the posts detail, when user click on a post in the feed,
they see the post on its own and can comment, edit and delete comments,
or edit and delete the post if its created by the user.
"""
class PostDetail(View):

    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()

        context = {
            'post': post,
            'form': form,
        }

        return render(request, 'post_detail.html', context)


"""
Views for edit a uploaded post, and using get_successs_url to rederict back
to the post detail template when user has submit the edit.
"""
class PostEdit(UpdateView):
    model = Post
    fields = ['body']
    template_name = 'post_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post_detail', kwargs={'pk':pk})


"""
Views for Delete a uploaded post from the feed.
"""
class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_feed')
