from django.urls import path
from .views import *
from apps.customer.views import send_message

# TODO badan url ha doros beshe ba estefade az id e cutomer
app_name = "manager"
urlpatterns = [
    path('home-page', index, name='index'),
    path('profile', manager_profile_view, name='manger_profile'),
    path('edit-profile', update_manager_profile, name='manager_edit'),
    path('send-message', send_message, name='send_message'),
]
