from django.contrib import admin

from apps.accounts.models import Manager, MyUser


# class ManagerAdmin(admin.ModelAdmin):
#     list_display = ('user')
#
#
# admin.site.register(Manager, ManagerAdmin)


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('is_manager', 'is_customer', 'is_employee', 'id')


admin.site.register(MyUser, MyUserAdmin)
