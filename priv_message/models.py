from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max


class Inbox(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='receiver')
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sender')
    body = models.TextField(max_length=500, blank=True, null=True)
    send_date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)


    def send_message(sender, receiver, body):
        sender_priv = Inbox(
            user=sender,
            sender=sender,
            receiver=receiver,
            body=body,
            read=True
        )
        sender_priv.save()

        receiver_priv = Inbox(
            user=receiver,
            sender=sender,
            receiver=receiver,
            body=body
        )
        receiver_priv.save()

        return sender_priv


    def get_message(user):
        users = []
        inbox = Inbox.objects.filter(user=user).values(
            'receiver').annotate(last=Max('send_date')).order_by('-last')
        for message in inbox:
            users.append({
                'user': User.objects.get(pk=message['receiver']),
                'last': message['last'],
                'unread': Inbox.objects.filter(
                    user=user, receiver__pk=message['receiver'], read=False).count()
            })
        return users
