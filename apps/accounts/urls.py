# from django.conf.urls import url
# from apps.accounts import views
#
# app_name = "accounts"
# urlpatterns = [
#     url(r'^signup/$', views.SignupView.as_view(), name='signup'),
#     url(r'^login/$', views.LoginView.as_view(), name='login'),
#     url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
#     url(r'^update_profile/$', views.UpdateProfileView.as_view(), name='update_profile'),
#
#     url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#         views.activate, name='activate'),
#     url(r'^email_sent$', views.email_sent, name='email_sent'),
#     url(r'^email_confirm$', views.email_confirm, name='email_confirm'),
#     url(r'^email_invalid$', views.email_invalid, name='email_invalid'),
# ]


from django.conf.urls import url

from apps.accounts.views import login_user
from . import views
from tahlil import settings
from django.conf.urls.static import static
from apps.customer.views import customer_home_view
app_name = "accounts"
urlpatterns = [
    url(r'^$', login_user, name='login'),
    url(r'^register/$', views.sign_up, name='register'),
    url(r'^customer/customer_home', customer_home_view,  name='customer_home'),
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
