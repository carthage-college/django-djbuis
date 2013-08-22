#You need all the imports below
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory

#Gotta make sure to include your form and model!
from djbuis.keyrequest.form import ModelForm
from djbuis.keyrequest.models import Keys

def create(request):
	if request.POST: #If we do a POST
		form = ModelForm(request.POST) #Scrape the data from the form and save it in a variable
		if form.is_valid(): #If the form is valid
			form_instance = form.save() #Save the form data to the datbase table
			return HttpResponseRedirect('http://Google.com')
	else:
		form = ModelForm()
	return render(request, 'keyrequest/form.html', {'form': form})

def submitted(request):
	return render(request, 'keyrequest/form.html')
