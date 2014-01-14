from django.conf.urls import patterns,url

urlpatterns = patterns('testuser.views',
	url(r'^testuser/index/$','testuser_index'),
	url(r'^testuser/login/$','testuser_login'),
	)	