from django.conf.urls import url
from django.urls import path

from apps.accounts.views import login_user
from . import views
from tahlil import settings
from django.conf.urls.static import static
from apps.customer.views.currency_views import customer_home_view
from django.contrib.auth.views import password_reset, password_reset_complete, password_reset_confirm, password_reset_done

app_name = "accounts"
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', login_user, name='login'),
    path('register/', views.sign_up, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('reset/done/', password_reset_complete, name='password_reset_complete'),
    path('password_reset/', password_reset, name='password_reset'),
    path('password_reset/done/', password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, name='password_reset_confirm'),

    path('customer/customer_home', customer_home_view,  name='customer_home'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
