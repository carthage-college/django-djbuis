#You need all the imports below. Be sure to change the names of the models and forms accordingly!
from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from djbuis.permitcheck.forms import SearchForm
from djzbar import settings
from djbuis import settings
from djzbar.utils.informix import do_sql
from django.core.mail import send_mail
from django.core.context_processors import csrf
from django.template import RequestContext  # For CSRF
from django.views.decorators.csrf import csrf_exempt

def index(request):
    if request.POST: #If we do a POST
        form = SearchForm(request.POST) #Scrape the data from the form and save it in a variable
        if form.is_valid(): #If the form is valid
            sql = """SELECT veh_rec.*, id_rec.firstname, id_rec.lastname
                    FROM veh_rec
                    LEFT JOIN id_rec
                    ON veh_rec.id = id_rec.id
                    WHERE veh_rec.id = CAST('%(isearch)s' AS int)
                    OR veh_rec.license = '%(lsearch)s'
                    OR veh_rec.decal = '%(psearch)s'""" % (form.cleaned_data)
            results = do_sql(sql, key=settings.INFORMIX_DEBUG, earl=settings.INFORMIX_EARL)
            return render(request, 'permitcheck/results.html', {
                'result': results.first(),
            })
    else:
        form = SearchForm()
        
    return render(request, 'permitcheck/home.html', {
        'form': form,
    })


@csrf_exempt
def lsearch(request):
    sql = """SELECT license
            FROM veh_rec
            WHERE license LIKE '%%%s%%'""" % (request.POST['license'])
    results = do_sql(sql)
    results_string = ''
    for thing in results:
        temp = thing['license']
        if temp:
            if results_string:
                results_string = results_string + ','
            results_string = results_string + temp
    return HttpResponse(results_string)


@csrf_exempt
def psearch(request):
    sql = """SELECT decal
            FROM veh_rec
            WHERE decal LIKE '%%%s%%'""" % (request.POST['permit'])
    results = do_sql(sql)
    results_string = ''
    for thing in results:
        temp = thing['decal']
        if temp:
            if results_string:
                results_string = results_string + ','
            results_string = results_string + temp
    return HttpResponse(results_string)


@csrf_exempt
def isearch(request):
    sql = """SELECT id
            FROM veh_rec
            WHERE CAST(id AS varchar(32)) LIKE '%%%s%%'""" % (request.POST['id'])
    results = do_sql(sql)
    results_string = ''
    for thing in results:
        temp = thing['id']
        if temp:
            if results_string:
                results_string = results_string + ','
            results_string = results_string + str(temp)
    return HttpResponse(results_string)