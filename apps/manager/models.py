from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from datetime import date

from apps.core.models import SystemAccounts
from apps.customer.models import DomesticCardField

from apps.accounts.models import MyUser, SEX_CHOICES


class Manager(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True, unique=True)
    system_accounts = models.ForeignKey(SystemAccounts, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=SEX_CHOICES, default='female')
    national_id = models.CharField(max_length=10, default='')
    phone = models.CharField(max_length=12, unique=False, default='')

    def __str__(self):
        return self.first_name


class ManagerAddedExams(models.Model):
    exam_title = models.CharField(max_length=30)
    dollar_cost = models.FloatField(default=0, validators=[MaxValueValidator(1000), MinValueValidator(1)])
    site_url = models.URLField(null=True, blank=True)
    image_url = models.URLField()

    def str(self):
        return self.exam_title
