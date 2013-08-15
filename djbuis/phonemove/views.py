from django.shortcuts import render
from django.http import HttpResponse
from form import ModelForm
from djbuis.phonemove.models import Phone
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.core.mail import send_mail

def create(request):
	if request.POST:
		form = ModelForm(request.POST)
		if form.is_valid():
			send_mail('Phone Change Form', form.to_mail, 'this', ['uberelitepwnzor@gmail.com'], fail_silently=False)
			form_instance = form.save()
			return HttpResponseRedirect('http://ddp.nintendo.com')
	else:
		form = ModelForm()
	return render(request, 'phonemove/form.html', {'form': form})

def submitted(request):
	return render(request, 'phonemove/form.html')
