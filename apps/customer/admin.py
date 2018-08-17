from django.contrib import admin
from apps.customer.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name')


admin.site.register(Customer,CustomerAdmin)
