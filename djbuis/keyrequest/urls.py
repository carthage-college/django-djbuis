from django.conf.urls import patterns, include, url #Need this

#This is where I put all the 'views' associated with this form
urlpatterns = patterns('djbuis.keyrequest.views', #Look in my 'views.py' file too
	url(r'^$', 'create', name="create"), #If I have nothing else appended to my url, I go into my 'views.py' file and call the 'create' function
)	
