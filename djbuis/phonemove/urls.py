from django.conf.urls import patterns, include, url

#This is where we add all of our 'views' of our project
urlpatterns = patterns('djbuis.phonemove.views',
    url(r'$', 'index', name="index"), #If I have nothing else appended to my url, I go into my 'views.py' file and call the 'index' function
)    
