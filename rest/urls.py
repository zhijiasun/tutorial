from django.conf.urls import url,patterns
from rest import views

urlpatterns = patterns('',
    url(r'^register/user/$',views.register_user),        
    url(r'^list/polls/$',views.operate_poll)
)
