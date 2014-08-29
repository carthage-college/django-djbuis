from django.conf.urls import patterns, url #Need this

#Where I put all the 'views' associated with this form
urlpatterns = patterns('djbuis.permitcheck.views', #Look in my 'views.py' file too
    url(r'^$', 'index', name='index'), #If I have nothing else appended to my url, I go into my 'views.py' file and call the 'index' function
    url(r'lsearch$', 'lsearch', name='lsearch'),
    url(r'psearch$', 'psearch', name='psearch'),
    url(r'isearch$', 'isearch', name='isearch'),
)