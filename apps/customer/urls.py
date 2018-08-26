from django.conf.urls import include
from django.urls import path
from .views import *

# TODO badan url ha doros beshe ba estefade az id e cutomer
app_name = "customer"
urlpatterns = [
    path('home-page', index, name='index'),
    path('profile', customer_profile_view, name='customer_profile'),
    path('edit-profile', update_customer_profile, name='edit_profile'),
    path('send-message', send_message, name='send_message'),
    path('', customer_home_view, name='customer_home'),
    path('dashboard/', customer_dashboard_view, name="dashboard"),
    path('dashboard/messages', message_dashboard_view, name='message dashboard'),
    path('dashboard/transactions', transaction_dashboard_view, name='transaction dashboard'),
    path('dashboard/orders', order_dashboard_view, name='ored dashboard'),
    path('transactions/', include('apps.transactions.urls'), name='customer_transactions'),

]
