from django.contrib import admin
from apps.manager.models import Manager


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name')


admin.site.register(Manager, ManagerAdmin)
