from django.urls import path
from apps.kapo.views import *

urlpatterns = [
    path('contact-us/', contact_us_view, name='contact-us'),
    path('about-us/', about_us_view, name='about-us'),
    path('policy/', policy_view, name='policy'),
]
