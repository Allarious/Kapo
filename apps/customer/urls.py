from django.conf.urls import url

from apps.accounts.views import login_user
from apps.customer.views import *
from . import views

app_name = "customer"
url(r'^profile/(?P<customer_id>\d+)/$', profile_view, name='customer_profile'),
