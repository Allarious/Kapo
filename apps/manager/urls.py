from django.urls import path
from .views import *
from apps.customer.views import send_message

# TODO badan url ha doros beshe ba estefade az id e cutomer
app_name = "manager"
urlpatterns = [
    path('home-page', index, name='index'),
    path('profile', manager_profile_view, name='manger_profile'),
    path('edit-profile', update_manager_profile, name='manager_edit'),
    path('send-message', send_message, name='send_message'),
    path('check-transactions', manager_check_transaction_view, name='manager_checking_transactions'),
    path('check-owner-transactions', manager_transaction_owner_view, name='manager_checking_owner_transactions'),
    path('all-system-transactions', manager_all_system_transactions_view, name='employee_checking_owner_transactions'),
]

# TODO bayad mogheyi ke tarakonesh barresish tamum mishe checke checkingesh false beshe/
# TODO / verfyesham az null beshe ya false ya true unjuri mifahmim barresi shode ya na
