from django.contrib import admin
from .models import Configuration


# Register your models here.
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')


admin.site.register(Configuration, ConfigurationAdmin)
