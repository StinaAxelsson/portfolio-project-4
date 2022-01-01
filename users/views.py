from django.shortcuts import render
from django.views import View
from .models import Profile



class ProfileView(View):
    
    def get(self, request, *args, **kwargs):
        user = Profile.objects.all()

        context = {
            'profile': user,

        }

        return render(request, 'user_profile.html', context)