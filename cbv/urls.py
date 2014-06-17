from django.conf.urls import patterns,include,url
from views import *

urlpatterns = patterns('',
        url(r'^testtemplateview/$',TestTemplateView.as_view()),
        url(r'^testredirectview/$',TestRedirectView.as_view()),
        url(r'^testlistview/$',TestListView.as_view()),
    )
