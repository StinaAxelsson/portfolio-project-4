from django.urls import path
from .views import private_messages

urlpatterns = [
    path('inbox/', private_messages, name='messages'),
]