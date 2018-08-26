from django.contrib import admin
from apps.manager.models import *


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name')


admin.site.register(Manager, ManagerAdmin)


class ManagerAddedExamsAdmin(admin.ModelAdmin):
    list_display = ('exam_title', 'dollar_cost')


admin.site.register(ManagerAddedExams, ManagerAddedExamsAdmin)
