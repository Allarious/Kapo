from django.conf.urls import url

from apps.accounts.views import login_user
from apps.customer.views import *
from . import views

app_name = "customer"
urlpatterns = [
url(r'^profile/$', customer_profile_view, name='customer_profile'),
url(r'^home/$', customer_home_view, name='customer_home'),
]
