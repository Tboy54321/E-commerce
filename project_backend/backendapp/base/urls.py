from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('search/<str:pk>', views.search_results, name="searchresults"),
    path('user-sign-in/', views.userlogin, name='Userlogin'),
    path('user-sign-out/', views.userlogout, name='Userlogout'),
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
    path('settings/<str:pk>/', views.settings,  name='Settings'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
