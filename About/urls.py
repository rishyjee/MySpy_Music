from django.conf.urls import url
from . import views

app_name='About'

urlpatterns = [
    #/About/
    url(r'^$', views.IndexView.as_view(), name='index'),


    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #/About/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

#/About/album/add/
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),
#/About/album/update/
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
#/About/album/delete/
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

]
