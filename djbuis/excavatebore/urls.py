from django.conf.urls import patterns, url

urlpatterns = patterns('djbuis.excavatebore.views',
	url(r'^$', 'index', name='index'),
)
