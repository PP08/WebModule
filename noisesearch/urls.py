from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^upload_single/$', views.model_form_single, name='upload_single'),
    url(r'^upload_multiple/$', views.model_form_multiple, name='upload_multiple'),
]