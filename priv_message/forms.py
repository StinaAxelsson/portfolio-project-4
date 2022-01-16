from django import forms
from .models import Inbox, Thread

class InboxForm(forms.Form):
    username = forms.CharField(max_length=100, label='')

class MessageForm(forms.Form):
    message = forms.CharField(label='', max_length=500)