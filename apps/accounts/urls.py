from django.conf.urls import url
from apps.accounts import views

app_name = "accounts"
urlpatterns = [
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^update_profile/$', views.UpdateProfileView.as_view(), name='update_profile'),

    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^email_sent$', views.email_sent, name='email_sent'),
    url(r'^email_confirm$', views.email_confirm, name='email_confirm'),
    url(r'^email_invalid$', views.email_invalid, name='email_invalid'),
]
