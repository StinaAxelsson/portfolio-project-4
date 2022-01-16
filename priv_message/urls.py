from django.urls import path
from .views import InboxList, CreateInboxForm, Message, CreateMessage

urlpatterns = [
    path('chats/', InboxList.as_view(), name='inbox'),
    path('new/', CreateInboxForm.as_view(), name='priv-message'),
    path('chats/<int:pk>/', Message.as_view(), name='message'),
    path('send/', CreateMessage.as_view(), name='send'),
]

