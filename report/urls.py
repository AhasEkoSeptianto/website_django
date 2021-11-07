from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<tahun>[\w]+)/(?P<bulan>[\w]+)/$', views.data,name='data'),
    url(r'^(?P<tahun>[\w]+)/(?P<bulan>[\w]+)/create/$', views.datatambah,name='datatambah'),
    # url(r'^(?P<tahun>[\w]+)/(?P<bulan>[\w]+)/update/(?P<slug>[\W-]+)/$', views.viewupdate, name='dataupdate'),
    url(r'^(?P<tahun>[\w]+)/(?P<bulan>[\w]+)/create/delete/(?P<slug>[\w-]+)/$', views.delete, name='delete'),
    url(r'^(?P<tahun>[\w]+)/(?P<bulan>[\w]+)/delete/(?P<slug>[\w-]+)/$', views.delete, name='delete'),
    url(r'^(?P<tahun>[\w]+)/(?P<bulan>[\w]+)/update/(?P<slug>[\w]+)/$', views.update,name='dataupdate'),
    url(r'^$', views.index, name='index'),
]

app_name = 'report'