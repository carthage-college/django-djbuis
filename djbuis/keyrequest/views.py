from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from djbuis.keyrequest.form import KeyForm, InfoForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory, BaseFormSet #For formsets
from django.core.context_processors import csrf
from django.template import RequestContext  # For CSRF

def create(request):
    #For info on setting up formsets, see this link: http://goo.gl/Oz53K2
    #This is a template that says how many forms are required in the set.
    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                self.forms[0].empty_permitted = False
    KeyFormSet = formset_factory(KeyForm, formset=RequiredFormSet)
    if request.POST:
        form = InfoForm(request.POST)
        key_formset = KeyFormSet(request.POST, prefix ='key_stuff')
        if form.is_valid() and key_formset.is_valid():
            form_instance = form.save()
            for f in key_formset:
                key = f.save(commit=False)
                key.list = form_instance
                key.save()
            form = InfoForm()
            key_formset = KeyFormSet(prefix='key_stuff')
            return HttpResponseRedirect (reverse_lazy("submitted"))
    else:
        form = InfoForm()
        key_formset = KeyFormSet(prefix='key_stuff')
    
    # For CSRF protection
    # See http://docs.djangoproject.com/en/dev/ref/contrib/csrf/ 
    c = {'form': form,
         'key_formset': key_formset,
        }
    c.update(csrf(request))
    
    return render(request, 'keyrequest/design.html', {
        'form': form,
        'key_formset': key_formset,
    })

def submitted(request):
    return render(
        request, 'keyrequest/design.html'
    )