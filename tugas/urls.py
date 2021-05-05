from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    
    url(r'^(?P<semester>[\w]+)/(?P<matakuliah>[\w]+)/$', views.daftarTugas, name='daftarTugas'),
    url(r'^(?P<semester>[\w]+)/(?P<matakuliah>[\w]+)/create/$', views.create, name='create'),
    url(r'^(?P<semester>[\w]+)/(?P<matakuliah>[\w]+)/delete/(?P<id>[\w]+)/$', views.delete, name='delete'),
    url(r'^(?P<semester>[\w]+)/(?P<matakuliah>[\w]+)/update/(?P<id>[\w]+)/(?P<pertemuan>[\w]+)/$', views.update, name='update'),
    url(r'^$', views.index, name='index'),
]

app_name = 'tugas'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)