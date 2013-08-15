from django.conf.urls import patterns, include, url

urlpatterns = patterns('djbuis.maintenance.views',
	url(r'^$', 'create', name='create'),
)
