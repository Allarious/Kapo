from django.contrib import admin
from .models import *


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')


admin.site.register(Configuration, ConfigurationAdmin)
