from django.shortcuts import render
from django.http import HttpResponse
from forms import KeyForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory

def create(request):
    if request.POST:
        form = KeyForm(request.POST)
        if form.is_valid():
            form_instance = form.save()
            return HttpResponseRedirect (reverse_lazy("submitted"))
    else:
        form = KeyForm()
    return render(request, 'keyrequest/design.html', {'form': form})

def submitted(request):
    return render(
        request, 'keyrequest/design.html'
    )
