from django.contrib import admin

from apps.accounts.models import Manager, Employee

admin.register(Manager)
admin.register(Employee)