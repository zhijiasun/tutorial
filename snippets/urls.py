from django.conf.urls import patterns,url

urlpatterns = patterns('snippets.views',
	#url(r'^index/$','snippet_index'),
	url(r'^snippets/$','snippet_list2'),
	url(r'snippets/(?P<pk>[0-9]+)/$','snippet_detail'),
	)
