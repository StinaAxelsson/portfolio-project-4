from django.urls import path
from .views import PostList, PostDetail, PostEdit, PostDelete


urlpatterns = [
    path('', PostList.as_view(), name='post_feed'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('post/edit/<int:pk>', PostEdit.as_view(), name='post_edit'),
    path('post/delete/<int:pk>', PostDelete.as_view(), name='post_delete'),
]