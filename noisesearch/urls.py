from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^get_details/$', views.get_details, name='get_details'),
    url(r'^data_filter/$', views.data_filter, name='data_filter'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'noisesearch/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'home'}, name='logout'),
    url(r'^data_manager/$', views.data_manager, name='data_manager'),
    url(r'data_manager/pbs/(?P<pk>\d+)/$', views.get_detail_pbs, name='get_detail_pbs'),
    url(r'data_manager/prs/(?P<pk>\d+)/$', views.get_detail_prs, name='get_detail_prs'),
    url(r'data_manager/delete_data/$', views.delete_selected_data, name='delete_selected_data'),
    url(r'data_manager/change_state_single/$', views.change_state_single, name='change_state_single'),
]
