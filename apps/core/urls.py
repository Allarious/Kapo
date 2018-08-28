from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name ='index'),
    path('contact-us/', contact_us_view, name='contact-us'),
    path('about-us/', about_us_view, name='about-us'),
    path('policy/', policy_view, name='policy'),
    path('wages/', wages_list_view, name='wages'),
]
