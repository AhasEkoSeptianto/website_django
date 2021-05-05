from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<tahun>[\w]+)/(?P<bulan>[\w]+)/$', views.data,name='data'),
    url(r'^(?P<tahun>[\w]+)/(?P<bulan>[\w]+)/create/$', views.datatambah,name='datatambah'),
    url(r'^(?P<tahun>[\w]+)/(?P<bulan>[\w]+)/update/$', views.viewupdate, name='viewupdate'),
    url(r'^(?P<tahun>[\w]+)/(?P<bulan>[\w]+)/delete/(?P<id>[\w]+)/$', views.delete, name='delete'),
    url(r'^(?P<tahun>[\w]+)/(?P<bulan>[\w]+)/update/(?P<id>[\w]+)/$', views.update,name='dataupdate'),
    url(r'^$', views.index, name='index'),
]

app_name = 'report'