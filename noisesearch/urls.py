from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^upload_single/$', views.model_form_single, name='upload_single'),
    url(r'^get_details/$', views.get_details, name='get_details'),
    url(r'^data_filter/$', views.data_filter, name='data_filter'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'noisesearch/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'home'}, name='logout'),
    url(r'^data_manager/$', views.data_manager, name='data_manager'),
]