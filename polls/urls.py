from django.conf.urls import url,patterns
from polls import views

urlpatterns = patterns('',
 	url(r'^$',views.index,name='index'),
 	url(r'^(?P<poll_id>\d+)/$', views.detail,name='detail'),
 	url(r'^(?P<poll_id>\d+)/results/$',views.results,name='results'),
)
