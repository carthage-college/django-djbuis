# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic

from djbuis.excavatebore.models import ExcavateModel
from djbuis.excavatebore.forms import ExcavateForm

def index(request):
	if request.method == 'POST':
		form = ExcavateForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('http://google.com')
	else:
		form = ExcavateForm()
		
	return render(request, 'excavatebore/form.html', {
		'form': form,
	})
	
#def submitted(request):
#	return render(request, 'templates/excavatebore/submitted.html')
