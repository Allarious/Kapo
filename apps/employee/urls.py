
from django.urls import path
from .views import *

# TODO badan url ha doros beshe ba estefade az id e cutomer
app_name = "employee"
urlpatterns = [
    path('home-page', index, name='index'),
    path('profile', employee_profile_view, name='employee_profile'),
]