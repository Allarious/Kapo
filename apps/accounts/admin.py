from django.contrib import admin

from apps.accounts.models import MyUser, Message


# class ManagerAdmin(admin.ModelAdmin):
#     list_display = ('user')
#
#
# admin.site.register(Manager, ManagerAdmin)


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('is_manager', 'is_customer', 'is_employee', 'id')


admin.site.register(MyUser, MyUserAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'subject', 'message')


admin.site.register(Message, MessageAdmin)
