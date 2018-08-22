from django.db import models
from django.utils import timezone


# Create your models here.
class Configuration(models.Model):
    key = models.CharField(max_length=10)
    value = models.CharField(max_length=10)


class Transaction(models.Model):
    creation_time = models.DateTimeField(default=timezone.now)


