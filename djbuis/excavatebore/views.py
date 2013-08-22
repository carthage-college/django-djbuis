#I need all the imports below
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic

#Gotta make sure to include your form and model!
from djbuis.excavatebore.models import ExcavateModel
from djbuis.excavatebore.forms import ExcavateForm

def index(request):
	if request.method == 'POST': #If we do a POST
		form = ExcavateForm(request.POST) #Scrape the data from the form and save it in a variable
		if form.is_valid(): #If the form is valid
			form.save() #Save the form data to the datbase table
			return HttpResponseRedirect('http://google.com')
	else:
		form = ExcavateForm()
		
	return render(request, 'excavatebore/form.html', {
		'form': form,
	})
