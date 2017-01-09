from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def add_company(request, company_name, post_number, address):
    company = Company(company_name, post_number,address )
    company.save()
    return HttpResponse("<html><body>" + company_name + " is registered.</body></html>")
