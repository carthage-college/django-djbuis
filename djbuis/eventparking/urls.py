from django.conf.urls import patterns, include, url

urlpatterns = patterns('djbuis.eventparking.views',
	url(r'$', 'create', name='create'),
)
