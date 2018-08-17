# from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models


class MyUser(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)


SEX_CHOICES = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'), ('blank', 'Blank'))


class Manager(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)


class Employee(models.Model):
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

# class Profile(models.Model):
#     user = models.OneToOneField(MyUser, related_name='profile')
#     phone_number = models.CharField(max_length=11, null=True, blank=True, verbose_name=_('Mobile number‌'))
#     organization = models.CharField(max_length=128, null=False, blank=False, verbose_name=_('Organization‌'))
#     age = models.IntegerField(null=True, blank=True, verbose_name=_('Age‌'))
#     national_code = models.CharField(max_length=10, null=True, blank=True, verbose_name=_('National code‌'))
#     tel_number = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Telephone number‌'))
#
#
#     @property
#     def is_complete(self):
#         if self.phone_number is None:
#             return False
#         if self.age is None:
#             return False
#         if self.national_code is None:
#             return False
#         if self.tel_number is None:
#             return False
#         return True
#
#     def __str__(self):
#         return self.user.username
