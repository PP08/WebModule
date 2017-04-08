from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^upload_single/$', views.model_form_single, name='upload_single'),
    url(r'^test_ajax/$', views.test_ajax, name='test_ajax'),
]