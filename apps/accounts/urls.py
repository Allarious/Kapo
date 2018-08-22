from django.conf.urls import url

from apps.accounts.views import login_user
from . import views
from tahlil import settings
from django.conf.urls.static import static
from apps.customer.views import customer_home_view
from django.contrib.auth.views import password_reset_complete, password_reset, password_reset_done, \
    password_reset_confirm

app_name = "accounst"
urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url(r'^login', login_user, name='login'),
                  url(r'^register/$', views.sign_up, name='register'),
                  url(r'^logout', views.user_logout, name='logout'),
                  url(r'^password_reset_complete/', password_reset_complete, name='password_reset_complete'),
                  url(r'^password_reset/', password_reset, name='password_reset'),
                  url(r'^password_reset_done', password_reset_done, name='password_reset_done'),
                  url(
                      r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                      password_reset_confirm, name='password_reset_confirm'),

                  url(r'^customer/customer_home', customer_home_view, name='customer_home'),
                  # url(r'^login_user/$', views.login_user, name='login_user'),
                  # url(r'^logout_user/$', views.logout_user, name='logout_user'),
                  # url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
                  # url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
                  # url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
                  # url(r'^create_album/$', views.create_album, name='create_album'),
                  # url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
                  # url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
                  # url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
                  # url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
