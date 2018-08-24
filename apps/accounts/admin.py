from django.contrib import admin

from apps.accounts.models import Manager, Employee, MyUser


# class ManagerAdmin(admin.ModelAdmin):
#     list_display = ('user')
#
#
# admin.site.register(Manager, ManagerAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name')


admin.site.register(Employee,EmployeeAdmin)


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('is_manager', 'is_customer', 'is_employee')


admin.site.register(MyUser, MyUserAdmin)
