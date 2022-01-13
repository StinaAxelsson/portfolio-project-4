from django.urls import path
from .views import Threads

urlpatterns = [
    path('inbox/', Threads, name='messages'),
]