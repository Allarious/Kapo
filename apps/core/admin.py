from django.contrib import admin
from .models import *


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')


admin.site.register(Configuration, ConfigurationAdmin)


class SystemAccountsAdmin(admin.ModelAdmin):
    list_display = ('rial_amount_account', 'dollar_amount_account', 'euro_amount_account')


admin.site.register(SystemAccounts, SystemAccountsAdmin)
