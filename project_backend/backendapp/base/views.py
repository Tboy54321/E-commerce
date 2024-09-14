from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
context = [
    {"id": "1", "title": "Specializing in luxury vehicles."},
    {"id": "2", "title": "Expert car repair services."},
    {"id": "3", "title": "Trusted vehicle dealerships."}
]

def home(request):
    return render (request, 'homepage.html', {"context": context})

def search_results(request, pk):
    # name = None
    # for i in context:
    #     if i['id'] == pk:
    #         name = i
    # return render (request, 'searchresults.html', {"name": name})
    return render (request, 'searchresults.html')

def userlogin(request):
    return render (request, 'Userlogin.html')

def usereg(request):
    return render (request, 'Useregistration.html')

def aboutus(request):
    return render (request, 'Aboutus.html')

def companieslist(request):
    return render (request, 'Listofcompanies.html')

def companyreg(request):
    return render (request, 'Companyreg.html')

def contactcompany(request):
    return render (request, 'Contactcompany.html')

def companydashboard(request):
    return render (request, 'Companydashboard.html')

def companyprofile(request):
    return render (request, 'Companyprofile.html')

def usernotifcation(request):
    return render (request, 'Usernotification.html')

def companynotifcation(request):
    return render (request, 'Companynotification.html')

def contactus(request):
    return render (request, 'Contactus.html')