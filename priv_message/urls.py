from django.urls import path
from .views import InboxList, CreateInboxForm

urlpatterns = [
    path('chats/', InboxList.as_view(), name='inbox'),
    path('chats/start-chat', CreateInboxForm.as_view(), name='priv-message'),
]

