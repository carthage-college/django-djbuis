from django.shortcuts import render
from django.http import HttpResponse
from form import ModelForm
from models import Keys
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory

def create(request):
	if request.POST:
		form = ModelForm(request.POST)
		if form.is_valid():
			form_instance = form.save()
			return HttpResponseRedirect('http://Google.com')
	else:
		form = ModelForm()
	return render(request, 'keyrequest/design.html', {'form': form})

def submitted(request):
	return render(request, 'keyrequest/design.html')
