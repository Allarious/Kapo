from django.conf.urls import url

from apps.accounts.views import login_user
from apps.customer.views import *
from . import views

app_name = "customer"
urlpatterns = [
    url(r'^profile/$', customer_profile_view, name='customer_profile'),
    url(r'^$', customer_home_view, name='customer_home'),
    url(r'^rial-inc/$', customer_rial_inc_view, name='customer_rial_inc'),
    url(r'^exchange/$',customer_exchange_view, name="exchange_to_rial")
]
