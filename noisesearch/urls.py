from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^upload_single/$', views.model_form_single, name='upload_single'),
    url(r'^get_details/$', views.get_details, name='get_details'),
    url(r'^data_filter/$', views.data_filter, name='data_filter'),
]