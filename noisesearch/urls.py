from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^get_details_pbs/$', views.get_details_pbs, name='get_details'),
    url(r'^get_details_prs/$', views.get_details_prs, name='get_details'),
    url(r'^data_filter/$', views.data_filter, name='data_filter'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'noisesearch/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'home'}, name='logout'),
    url(r'^profile_manager/$', views.profile_manager, name='profile_manager'),
    url(r'^data_manager/$', views.data_manager, name='data_manager'),
    url(r'^change_password/$', views.change_password, name='change_password'),

    url(r'^data_manager/pbs/(?P<pk>\d+)/$', views.get_detail_pbs, name='get_detail_pbs'),
    url(r'^data_manager/prs/(?P<pk>\d+)/$', views.get_detail_prs, name='get_detail_prs'),
    url(r'^data_manager/prm/(?P<pk>\d+)/$', views.get_detail_prm, name='get_detail_prm'),
    url(r'^data_manager/pbm/(?P<pk>\d+)/$', views.get_detail_pbm, name='get_detail_pbm'),

    url(r'^data_manager/delete_data/$', views.delete_selected_data, name='delete_selected_data'),
    url(r'^data_manager/change_state_single/$', views.change_state_single, name='change_state_single'),
    url(r'^data_manager/change_state_multiple/$', views.change_state_multiple, name='change_state_multiple'),
    url(r'^graphs_pbs/$', views.renderGraphsPublic, name='render_graphs'),
    url(r'^graphs_prs/$', views.renderGraphsPrivate, name='render_graphs'),

    url(r'^multiple/$', views.multiple_map, name='multiple_map'),

    url(r'^test/$', views.test, name='test'),
]
