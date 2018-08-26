from django.core.exceptions import ValidationError
from django.db import models
from datetime import date
from apps.customer.models import DomesticCardField

from apps.accounts.models import MyUser, SEX_CHOICES


class Employee(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=SEX_CHOICES, default='male')
    birthday_date = models.DateField(default=date.today)
    national_id = models.CharField(max_length=10, default='')
    city = models.CharField(max_length=10, default='')
    country = models.CharField(max_length=20, default='Iran')
    address = models.CharField(max_length=100, default='Tehran')
    phone = models.CharField(max_length=12, unique=False, default='')
    domestic_card_number = DomesticCardField(unique=False, max_length=16, null=True)
    rial_wallet = models.FloatField(default=0)
    wage_per_month = models.FloatField(default=0)

    def clean(self):
        if self.rial_wallet < 0:
            raise ValidationError('You Dont have enough Rials')

    def __str__(self):
        return self.first_name
