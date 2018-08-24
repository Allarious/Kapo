
from django.urls import path
from .views import *

# TODO badan url ha doros beshe ba estefade az id e cutomer
app_name = "manager"
urlpatterns = [
    path('home-page', index, name='index'),
    path('profile', manager_profile_view, name='manger_profile'),
]