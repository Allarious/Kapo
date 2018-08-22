from django.conf.urls import url
from apps.kapo.views import *

urlpatterns = [
    url(r'^contact-us', contact_us_view, name='contact-us'),
    url(r'^about-us', about_us_view, name='about-us'),
    url(r'^policy', policy_view, name='policy'),
]
