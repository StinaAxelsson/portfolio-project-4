# Generated by Django 3.2 on 2022-01-01 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220101_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='media'),
        ),
    ]
