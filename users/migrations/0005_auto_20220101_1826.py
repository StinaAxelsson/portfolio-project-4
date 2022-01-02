# Generated by Django 3.2 on 2022-01-01 18:26

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
    ]
