from django.urls import path

from .views import *

app_name = "transactions"
urlpatterns = [

    path('', customer_transactions_view, name='customer transactions'),
    path('exam/', exam_transactions_view, name='exam transactions'),
    path('app-fee/', app_fee_transactions_view, name='application fee transactions'),
    path('foreign-pay/', foreign_pay_transactions_view, name='foreign pay transactions'),
    path('domestic-pay/', domestic_pay_transactions_view, name='domestic pay transactions'),
]
