from django.conf.urls import patterns, include, url
from keyrequest import views

urlpatterns = patterns('',
	url(r'^$', views.create, name="create"),
	url(r'^submitted/$', views.submitted),
)	
