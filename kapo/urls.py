from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import include, url


urlpatterns = [
    path('admin/', admin.site.urls),

]