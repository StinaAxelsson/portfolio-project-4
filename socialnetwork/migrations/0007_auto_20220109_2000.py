# Generated by Django 3.2 on 2022-01-09 20:00

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0006_alter_users_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upload',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], default=3),
        ),
    ]