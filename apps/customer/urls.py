from django.urls import path

from apps.customer.views import *

app_name = "customer"
urlpatterns = [
    path('profile', customer_profile_view, name='customer_profile'),
    path('', customer_home_view, name='customer_home'),
    path('rial-inc/', customer_rial_inc_view, name='customer_rial_inc'),
    path('exchange/', customer_exchange_view, name="exchange")
]
