from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render (request, 'homepage.html')

def another(request):
    return HttpResponse("Another requestssssss")
