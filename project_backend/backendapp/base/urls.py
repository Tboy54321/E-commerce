from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('search/<str:pk>', views.search_results, name="Search Results"),
    path('signin/', views.userlogin, name='Userlogin'),
    path('signup/', views.usereg, name='Usereg'),
    path('aboutus/', views.aboutus, name='Aboutus'),
    path('companies/', views.companieslist, name='Companies'),
    path('company-reg/', views.companyreg, name="Company reg"),
    path('contact-company/', views.contactcompany, name="Contact company"),
    path('company-dashboard/', views.companydashboard, name="Company dashboard"),
    path('company-profile/', views.companyprofile, name="Company profile"),
    path('user-notification/', views.usernotifcation, name="User notification"),
    path('company-notification/', views.companynotifcation, name="Company notification"),
    path('contactus/', views.contactus, name="Contact us"),
]
