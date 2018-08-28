
from django.urls import path
from .views import *
from apps.customer.views import send_message

# TODO badan url ha doros beshe ba estefade az id e cutomer
app_name = "employee"
urlpatterns = [
    path('home-page', index, name='index'),
    path('profile', employee_profile_view, name='employee_profile'),
    path('edit-profile', update_employee_profile, name='employee_edit'),
    path('check-transactions', employee_check_transaction_view, name='employee_checking_transactions'),
    path('check-owner-transactions', employee_transaction_owner_view, name='employee_checking_owner_transactions'),
    path('all-system-transactions', employee_all_system_transactions_view, name='employee_checking_owner_transactions'),
    path('send-message', send_message, name='send_message'),
    path('dashboard', employee_dashboard_view, name='dashboard'),
    path('dashboard/messages', message_dashboard_view, name='message dashboard'),
]