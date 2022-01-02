from django.shortcuts import render, redirect
from django.views import View
from .models import Profile


class ProfileView(View):
    
    def get(self, request, *args, **kwargs):
        user = Profile.objects.all()

        context = {
            
            'user': user,

        }
      
        return render(request, 'user_profile.html', context)