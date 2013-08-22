#I need all the imports below
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

#Include the form itself
from forms import ParkingForm

# Create your views here.	
def index(request):
	if request.POST: #If we do a POST
		form = ParkingForm(request.POST) #Scrape the data from the form and save it in a variable
		if form.is_valid(): #If the form is valid
			form.save() #Save the form data to the datbase table
			return HttpResponseRedirect('http://google.com')
		
	else:
		form = ParkingForm()
	return render(request, 'eventparking/form.html', {
		'form': form
	})
