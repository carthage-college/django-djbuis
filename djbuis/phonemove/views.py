#I need all the imports below
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail

#Import these! Might not need 'PhoneModel'..
from djbuis.phonemove.form import PhoneForm
from djbuis.phonemove.models import PhoneModel


def index(request):
    if request.POST: #If we do a POST
        form = PhoneForm(request.POST) #Scrape the data from the form and save it in a variable
        if form.is_valid(): #If the form is valid
            send_mail('Phone Change Form', form.to_mail(), 'Sender address', ['uberelitepwnzor@gmail.com'], fail_silently=False)
            form.save()
            form = PhoneForm()
            submitted = True
            return render(request, 'phonemove/form.html', {
        'form': form,
        'submitted': submitted
    })
    else:
        form = PhoneForm()
        
    return render(request, 'phonemove/form.html', {
        'form': form
    })

