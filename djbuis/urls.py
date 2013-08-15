from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^keyrequest/', include('djbuis.keyrequest.urls')),
    url(r'^excavatebore/', include('djbuis.excavatebore.urls')),
    url(r'^eventparking/', include('djbuis.eventparking.urls')),
    url(r'^maintenance/', include('djbuis.maintenance.urls')),
    url(r'^phonemove/', include('djbuis.phonemove.urls')),
)
