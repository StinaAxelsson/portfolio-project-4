from django.db import models
from dj.choices import Choices, Choice
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)


class Gender(Choices):
    male = Choice("male")
    female = Choice("female")
    other = Choice("other")

class Users(models.Model):
    user = models.OneToOneField(
        User,
        primary_key=True,
        verbose_name='user',
        related_name='profile',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50, blank=True, null=True)
    picture = CloudinaryField('image', default='placeholder')
    birthday = models.DateField(blank=True, null=True)
    gender = models.IntegerField(choices=Gender(),default=Gender.other.id)
    location = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
"""models.ImageField(upload_to='profile_images', default='profile_images/default_profile.png', blank=True)"""