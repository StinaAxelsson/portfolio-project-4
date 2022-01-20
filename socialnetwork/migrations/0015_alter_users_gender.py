# Generated by Django 3.2 on 2022-01-12 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0014_alter_users_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], default='other'),
        ),
    ]
