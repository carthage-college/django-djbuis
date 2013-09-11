#You need all the imports below
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory

#Gotta make sure to include your form and model!
from djbuis.keyrequest.form import KeyForm, OtherForm, RequiredFormSet
from djbuis.keyrequest.models import KeyModel, OtherModel

'''
def create(request):
    if request.POST: #If we do a POST
        form = ModelForm(request.POST) #Scrape the data from the form and save it in a variable
        if form.is_valid(): #If the form is valid
            form_instance = form.save() #Save the form data to the datbase table
            form = ModelForm()
            submitted = True
            return render(request, 'keyrequest/form.html', {'form': form, 'submitted': submitted})
    else:
        form = ModelForm()
    return render(request, 'keyrequest/form.html', {'form': form})
'''

def create(request):
    KeyFormSet = formset_factory(KeyForm, extra=1, formset=RequiredFormSet)
    form = OtherForm(request.POST)
    
    if request.method == 'POST':
        
        formset = KeyFormSet(request.POST, prefix='Key')
 
        if 'add' in request.POST:
            lists=[]
            for i in range(0,int(formset.data['Key-TOTAL_FORMS'])):
                lists.append({
                    'building': formset.data['Key-%s-building' % (i)],
                    'room_number': formset.data['Key-%s-room_number' % (i)],
                    'key_code_if_known': formset.data['Key-%s-key_code_if_known' % (i)],
                    'issued_to': formset.data['Key-%s-issued_to' % (i)]
                })
            formset = KeyFormSet(prefix='Key', initial=lists)
            form._errors={}
        else:
            if formset.is_valid() and form.is_valid():
                
                form.save()
                form = OtherForm()
                
                for f in formset: #This is how we save formset data, since there are multiple forms in a formset
                
                    if f.clean():
                        
                        (obj, created) = KeyModel.objects.get_or_create(
                            building=f.cleaned_data['building'],
                            room_number=f.cleaned_data['room_number'],
                            key_code_if_known=f.cleaned_data['key_code_if_known'],
                            issued_to=f.cleaned_data['issued_to']
                        )
                        
                return HttpResponseRedirect('http://google.com')
    else:
        formset = KeyFormSet(prefix='Key')
        form = OtherForm()
        
    return render(request, 'keyrequest/form.html', {
        'formset': formset,
        'form': form
    })
