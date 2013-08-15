from django.shortcuts import render
from django.http import HttpResponse
from djbuis.keyrequest.form import ModelForm
from djbuis.keyrequest.models import Keys
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
	return render(request, 'keyrequest/form.html', {'form': form})

def submitted(request):
	return render(request, 'keyrequest/form.html')
