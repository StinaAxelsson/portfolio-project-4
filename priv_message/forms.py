from django import forms
from .models import Inbox, Thread


class InboxForm(forms.Form):
    username = forms.CharField(max_length=100, label='inbox-field')

class MessageForm(forms.Form):
    message = forms.CharField(
        label='', 
        max_length=500,
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Write a message here...'
        })
    )
