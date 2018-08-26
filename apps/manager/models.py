from django.core.exceptions import ValidationError
from django.db import models
from datetime import date
from apps.customer.models import DomesticCardField

from apps.accounts.models import MyUser, SEX_CHOICES


class Manager(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=SEX_CHOICES, default='male')
    national_id = models.CharField(max_length=10, default='')
    phone = models.CharField(max_length=12, unique=False, default='')

    def __str__(self):
        return self.first_name
