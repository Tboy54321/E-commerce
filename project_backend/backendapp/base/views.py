from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import RegForm, LoginForm
from .models import Companies


# Create your views here.
context = [
    {"id": "1", "title": "Specializing in luxury vehicles."},
    {"id": "2", "title": "Expert car repair services."},
    {"id": "3", "title": "Trusted vehicle dealerships."}
]

def home(request):
    companies = Companies.objects.all()
    context = {'companies': companies}
    return render (request, 'homepage.html', context)

def search_results(request, pk):
    company = Companies.objects.get(id=pk)
    # print(name)
    return render (request, 'searchresults.html', {"company": company})
    # return render (request, 'searchresults.html')

def userlogin(request):
    formss = LoginForm()

    if request.method == "POST":
        formss = LoginForm(request.POST)
        if formss.is_valid():
            formss.save()
            return redirect('Home')
        
    context = {'form': formss}
    return render (request, 'Userlogin.html', context)

def usereg(request):
    return render (request, 'Useregistration.html')

def aboutus(request):
    return render (request, 'Aboutus.html')

def companieslist(request):
    return render (request, 'Listofcompanies.html')

def companyreg(request):
    forms = RegForm()

    if request.method == "POST":
        forms = RegForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('Home')

    context = {'form': forms}
    return render (request, 'Companyreg.html', context)


def updateCompanyInfo(request, pk):
    company = Companies.objects.get(id=pk)
    form = RegForm(instance=company)
    if request.method == "POST":
        form = RegForm(request.POST, instance=company)
        if form.is_valid:
            form.save()
            return redirect('Home')
    context = {'form': form}
    return render(request, 'Companyreg.html', context)


def deleteCompanyInfo(request, pk):
    company = Companies.objects.get(id=pk)
    context = {'obj': company}
    if request.method == 'POST':
        company.delete()
        return redirect('Home')

    return render(request, 'delete.html', context)
    
    

def contactcompany(request):
    return render (request, 'Contactcompany.html')

def companydashboard(request):
    return render (request, 'Companydashboard.html')

def companyprofile(request):
    companies = Companies.objects.all()
    context = {'companies': companies}
    return render (request, 'Companyprofile.html', context)

def usernotifcation(request):
    return render (request, 'Usernotification.html')

def companynotifcation(request):
    return render (request, 'Companynotification.html')

def contactus(request):
    return render (request, 'Contactus.html')