from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    
    # url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^bright$', views.brightnees(), name='brightnees'),
    url(r'^store$', views.view_store, name='store'),
    url(r'^info$', views.view_info, name='info'),
    url(r'^history$', views.view_history, name='history'),
    url(r'^set_on_off$', views.view_set_on_off, name='set_on_off'),
    # url(r'^set_on_off_google$', views.view_set_on_off_google, name='set_on_off_google'),
    url(r'^get_on_off$', views.view_get_on_off, name='get_on_off'),
]
