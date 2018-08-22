from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import password_reset_complete, password_reset, password_reset_done, \
    password_reset_confirm

from apps.accounts.views import login_user, index

urlpatterns = [
    path('', include('apps.kapo.urls'), name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('customer/', include('apps.customer.urls')),

    path('login/', login_user, name='login'),
    path('reset/done/', password_reset_complete, name='password_reset_complete'),
    path('password-reset/', password_reset, name='password_reset'),
    path('password-reset/done/', password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm, name='password_reset_confirm'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
