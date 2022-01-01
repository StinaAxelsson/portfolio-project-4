from django.contrib import admin
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):

    list_display = (
        'user', 'image', 'first_name', 'last_name', 'birth_date', 'bio'
        )
    summernote_fields = ('bio')