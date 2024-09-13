from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('search/<str:pk>', views.search_results, name="Search Results"),
    path('signin/', views.userlogin, name='Userlogin'),
    path('signup/', views.usereg, name='Usereg'),
    path('aboutus/', views.aboutus, name='Aboutus'),
    path('companies/', views.companieslist, name='Companies')
]
