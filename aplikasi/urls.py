from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/$', views.add, name='tambah'),
    url(r'^(?P<data>[\w-]+)/$',views.listdata,name='listdata'),
    url(r'^$', views.index , name='index'),
]

app_name = 'aplikasi'