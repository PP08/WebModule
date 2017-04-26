from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    url(r'^token-auth/$', obtain_auth_token),
    url(r'^private_single/$', views.PrivateSingle.as_view(), name='private_single'),
    url(r'^public_single/$', views.PublicSingle.as_view(), name='public_single'),
    url(r'^private_multiple/$', views.PrivateMultiple.as_view(), name='private_multiple'),
    url(r'^public_multiple/$', views.PublicMultiple.as_view(), name='public_multiple'),
]
