from django.urls import path
from .views import Search
from socialnetwork.views import UserProfile

urlpatterns = [
    path('result/', Search.as_view(), name='search_user'),
    path('result/<int:pk>', UserProfile.as_view(), name='search_user'),
]