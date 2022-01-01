from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('username', 'status', 'created_on', 'content')
    search_fields = ['username', 'content']
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
