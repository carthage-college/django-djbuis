from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from forms import ParkingForm

# Create your views here.
def submitted(request):
	return render(request, 'other/submitted.html')
	
def create(request):
	if request.POST:
		form = ParkingForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('http://google.com')
		
	else:
		form = ParkingForm()
	return render(request, 'eventparking/form.html', {'form': form})
