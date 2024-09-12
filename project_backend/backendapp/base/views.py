from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render (request, 'homepage.html')

def search_results(request):
    return render (request, 'searchresults.html')
