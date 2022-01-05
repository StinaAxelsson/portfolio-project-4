from django.urls import path
from .views import PostListView, PostDetail


urlpatterns = [
    path('', PostListView.as_view(), name='post_feed'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
]