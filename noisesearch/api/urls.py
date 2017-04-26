from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    url(r'^token-auth/$', obtain_auth_token),
    url(r'^privateSingle/$', views.PrivateSingle.as_view(), name='private_single'),
    url(r'^publicSingle/$', views.PublicSingle.as_view(), name='public_single'),
    url(r'^privateMultiple/$', views.PrivateMultiple.as_view(), name='private_multiple'),
    url(r'^publicMultiple/$', views.PublicMultiple.as_view(), name='public_multiple'),
]
