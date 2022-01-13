from django.urls import path
from .views import Messages

urlpatterns = [
    path('inbox/', Messages.as_view(), name='messages'),
]