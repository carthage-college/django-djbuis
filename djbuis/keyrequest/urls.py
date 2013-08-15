from django.conf.urls import patterns, include, url

urlpatterns = patterns('djbuis.keyrequest.views',
	url(r'^$', 'create', name="create"),
)	
