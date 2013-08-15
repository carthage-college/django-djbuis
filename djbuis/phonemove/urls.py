from django.conf.urls import patterns, include, url

urlpatterns = patterns('djbuis.phonemove.views',
	url(r'^$', 'create', name="create"),
)	
