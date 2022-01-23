# Generated by Django 3.2 on 2022-01-22 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('priv_message', '0004_auto_20220121_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inbox',
            name='read',
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('notis', models.IntegerField()),
                ('read', models.BooleanField(default=False)),
                ('notis_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notis_from', to=settings.AUTH_USER_MODEL)),
                ('notis_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notis_to', to=settings.AUTH_USER_MODEL)),
                ('pm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='priv_message.inbox')),
            ],
        ),
    ]
