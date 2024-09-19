from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('search/<str:pk>', views.search_results, name="searchresults"),
    path('user-sign-in/', views.userlogin, name='Userlogin'),
    path('company-sign-in/', views.companylogin, name='Companylogin'),
    path('user-sign-up/', views.usereg, name='Usereg'),
    path('aboutus/', views.aboutus, name='Aboutus'),
    path('companies/', views.companieslist, name='Companies'),
    path('company-reg/', views.companyreg, name="CompanyReg"),
    path('update-company/<str:pk>/', views.updateCompanyInfo, name="UpdateCompany"),
    path('delete-company/<str:pk>/', views.deleteCompanyInfo, name="DeleteCompany"),
    path('contact-company/', views.contactcompany, name="contact_company"),
    path('company-dashboard/<str:pk>', views.companydashboard, name="company_dashboard"),
    path('company-profile/', views.companyprofile, name="Company profile"),
    path('user-notification/', views.usernotifcation, name="User notification"),
    path('company-notification/', views.companynotifcation, name="Company-notification"),
    path('contactus/', views.contactus, name="Contact us"),
]
