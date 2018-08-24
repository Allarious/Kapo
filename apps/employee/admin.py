from django.contrib import admin
from apps.employee.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name')


admin.site.register(Employee,EmployeeAdmin)
