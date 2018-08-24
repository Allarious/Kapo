from django.conf.urls import include
from django.urls import path
from .views import *

# TODO badan url ha doros beshe ba estefade az id e cutomer
app_name = "customer"
urlpatterns = [
    path('home-page', index, name='index'),
    path('profile', customer_profile_view, name='customer_profile'),
    path('edit-profile', update_customer_profile, name='edit_profile'),
    path('', customer_home_view, name='customer_home'),
    path('rial-inc/', customer_rial_inc_view, name='customer_rial_inc'),
    path('exchange/', customer_exchange_view, name="exchange"),
    path('transactions/', include('apps.transactions.urls'), name='customer_transactions'),

]
