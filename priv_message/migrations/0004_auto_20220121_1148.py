# Generated by Django 3.2 on 2022-01-21 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priv_message', '0003_auto_20220115_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='read',
        ),
        migrations.AddField(
            model_name='inbox',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
