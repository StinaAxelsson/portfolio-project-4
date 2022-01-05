from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '2',
            'placeholder': 'Whats on your mind today?...'
        })
    )

    class Meta:
        model = Post
        fields = ['body']