
from . import views
from django.contrib import admin
from django.conf.urls import include, url
from apps.customer import urls as customer_urls

urlpatterns = [
    url(r'^', include(customer_urls)),

]