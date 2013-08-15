from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from djbuis.maintenance.forms import MaintenanceForm


# Create your views here.
def submitted(request):
	return render(request, 'other/submitted.html')
	
def create(request):
	if request.POST:
		form = MaintenanceForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('http://google.com')
			
	else:
		form = MaintenanceForm()
	return render(request, 'maintenance/form.html', {'form': form})
