from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models


class MyUser(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_not_banned = models.BooleanField(default=True)


class Message(models.Model):
    sender = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='receiver')
    subject = models.CharField(max_length=40)
    message = models.TextField(null=True, blank=True)
    read = models.BooleanField(default=False)


NOTIFICATION_TYPES = (
('message', 'Message'), ('transaction', 'Transaction'), ('order', 'Order'), ('feature', 'Feature'),
('insufficient money', ' Insufficient Money'))
SEX_CHOICES = (('male', 'Male'), ('female', 'Female'), ('other', 'Non Binary'))


class Notification(models.Model):
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='owner')
    type = models.CharField(max_length=10, choices=NOTIFICATION_TYPES)
    seen = models.BooleanField(default=False)


class Inform(models.Model):
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=400)

#
# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles
#
# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
