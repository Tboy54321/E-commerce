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

def search_results(request):
    return render (request, 'searchresults.html')

def userlogin(request):
    return render (request, 'userlogin.html')

def usereg(request):
    return render (request, 'useregistration.html')