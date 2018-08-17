from django.db import models

from apps.accounts.models import MyUser, SEX_CHOICES


class Customer(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=SEX_CHOICES, default='Male')
    day = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    nationalId = models.CharField(max_length=10)
    city = models.CharField(max_length=10, default='blank')
    address = models.CharField(max_length=100, default='st')
    phone = models.CharField(max_length=12)
