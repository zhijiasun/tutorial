from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('snippets.urls')),
    url(r'^',include('testuser.urls')),
    url(r'^',include('formtest.urls')),
    url(r'cbv/',include('cbv.urls')),
    url(r'^polls/',include('polls.urls')),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'accounts/',include('registration.backends.default.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^',include('rest.urls')),
    url(r'^weblog/',include('zinnia.urls')),
    url(r'^comments/',include('django.contrib.comments.urls')),
)
