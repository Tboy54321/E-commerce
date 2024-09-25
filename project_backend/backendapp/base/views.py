from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db import IntegrityError
# from django.http import HttpResponse
from .form import RegForm, LoginForm, UserForm
from .models import Companies, CustomUser


# Create your views here.
# context = [
#     {"id": "1", "title": "Specializing in luxury vehicles."},
#     {"id": "2", "title": "Expert car repair services."},
#     {"id": "3", "title": "Trusted vehicle dealerships."}
# ]

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    companies = Companies.objects.filter(
        Q(name__icontains=q)
    )
    context = {'companies': companies}
    return render (request, 'homepage.html', context)


def search_results(request, pk):
    company = Companies.objects.get(id=pk)
    # print(name)
    return render (request, 'searchresults.html', {"company": company})
    # return render (request, 'searchresults.html')


def userlogin(request):
    if request.user.is_authenticated:
        return redirect('Home')

    if request.method == "POST":
        login_input = request.POST.get('username')
        password = request.POST.get('password')

        if '@' in login_input:
            try:
                user = CustomUser.objects.get(email=login_input)
                username = user.username
            except:
                messages.error(request, 'Email does not exist')
                return redirect ('Userlogin')
        elif login_input == "":
            messages.error(request, "Please fill in username or email")
            return redirect ('Userlogin')
        elif password == "":
            messages.error(request, "Please fill in your password")
            return redirect ('Userlogin')
        else:
            try:
                user = CustomUser.objects.get(username=login_input)
                username = login_input
            except:
                messages.error(request, 'Username does not exist')
                return redirect ('Userlogin')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect ('Home')
        else:
            messages.error(request, 'Invalid username or password')
        
    context = {}
    return render (request, 'Userlogin.html', context)
# Token-Based: Use JWT (JSON Web Tokens) or OAuth tokens for stateless authentication for logging in (DJANGO REST).
# Password Encryption: Compare hashed passwords to stored values during authentication.
# Login Attempts: Limit login attempts to prevent brute-force attacks.
# Multi-Factor Authentication (MFA): Implement an additional layer of security like SMS/Email/Authenticator app verification.


def userlogout(request):
    logout(request)
    return redirect ('Home')


def usereg(request):
    if request.user.is_authenticated:
        return redirect('Home')

    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                login(request, user)
                return redirect('Home')
            except IntegrityError:
                form.add_error('email', 'A user with this mail already exist.')
        else:
            messages.error(request, 'An error occured during registration')
    else:
        form = UserForm()

    context = {'form': form}    
    return render (request, 'Useregistration.html', context)


def companylogin(request):
    return render (request, 'Companylogin.html')


def aboutus(request):
    return render (request, 'Aboutus.html')


# Implementation of search functionality
def companieslist(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    companies = Companies.objects.filter(
        Q(name__icontains=q)
    )
    context = {'companies': companies}
    return render (request, 'Listofcompanies.html', context)


# Implementation of write functionality
@login_required(login_url='Userlogin')
def companyreg(request):
    forms = RegForm()

    if request.method == "POST":
        forms = RegForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('Home')

    context = {'form': forms}
    return render (request, 'Companyreg.html', context)


# Implementation of update functionality
@login_required(login_url='Userlogin')
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


# Implementation of delete functionality
@login_required(login_url='Userlogin')
def deleteCompanyInfo(request, pk):
    company = Companies.objects.get(id=pk)
    context = {'obj': company}
    if request.method == 'POST':
        company.delete()
        return redirect('Home')

    return render(request, 'delete.html', context)
    
@login_required(login_url='Userlogin')
def contactcompany(request):
    return render (request, 'Contactcompany.html')


@login_required(login_url='Userlogin')
def companydashboard(request, pk):
    company = Companies.objects.get(id=pk)
    context = {'company': company}
    return render (request, 'Companydashboard.html', context)


def companyprofile(request):
    companies = Companies.objects.all()
    context = {'companies': companies}
    return render (request, 'Companyprofile.html', context)

@login_required(login_url='Userlogin')
def usernotifcation(request):
    return render (request, 'Usernotification.html')

@login_required(login_url='Userlogin')
def companynotifcation(request):
    return render (request, 'Companynotification.html')

@login_required(login_url='Userlogin')
def contactus(request):
    return render (request, 'Contactus.html')

@login_required(login_url='Userlogin')
def settings(request):
    return render (request, 'usersettings.html')

def PasswordReset(request):
    return render (request, 'passwordreset.html')