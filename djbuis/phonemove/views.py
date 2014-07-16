from django.shortcuts import render
from django.http import HttpResponse
from form import ModelForm
from models import Phone
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.core.mail import send_mail

def create(request):
    if request.POST:
        form = ModelForm(request.POST)
        if 'email' in request.POST:
            send_mail('Subject here', "Body", 'confirmation.carthage.edu',
                ['zorpixfang@gmail.com'], fail_silently=False)
        if form.is_valid():
            form_instance = form.save()
            return HttpResponseRedirect('phonemove/design.html')
    else:
        form = ModelForm()
    return render(request, 'phonemove/design.html', {'form': form})

def submitted(request):
    return render(request, 'phonemove/design.html')
