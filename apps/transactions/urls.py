from django.urls import path

from .views import *

app_name = "transactions"
urlpatterns = [

    path('', customer_transactions_view, name='customer_transactions'),
    path('exam/', exam_transactions_view, name='exam_transactions'),
    path('app-fee/', app_fee_transactions_view, name='fee_transactions'),
]
