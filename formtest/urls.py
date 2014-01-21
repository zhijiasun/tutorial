from django.conf.urls import patterns,url

urlpatterns = patterns('formtest.views',
	url(r'^formtest/form/$','contact'),
	)