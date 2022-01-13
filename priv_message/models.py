from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from socialnetwork.models import Users


class PrivateMessage(models.Model):
    pm = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
