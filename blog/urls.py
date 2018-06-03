from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    
    # url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^store$', views.view_store, name='store'),
    url(r'^info$', views.view_info, name='info'),
    url(r'^history$', views.view_history, name='history'),
    url(r'^on_off$', views.view_on_off, name='on_off'),
    url(r'^on_off1$', views.view_on_off1, name='on_off1'),
]
