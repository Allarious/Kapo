from django.urls import path

from .views.currency_views import *
from .views.transaction_views import *

app_name = "customer"
urlpatterns = [
    path('profile', customer_profile_view, name='customer_profile'),
    path('', customer_home_view, name='customer_home'),
    path('rial-inc/', customer_rial_inc_view, name='customer_rial_inc'),
    path('exchange/', customer_exchange_view, name="exchange"),
    path('transactions/', customer_transactions_view, name='customer_transactions'),
    path('transactions/exam', exam_transactions_view, name='exam_transactions'),
]
