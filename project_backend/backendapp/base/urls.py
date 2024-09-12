from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('search/', views.search_results, name="Search Results"),
    path('signin/', views.userlogin, name='Userlogin'),
    path('signup/', views.usereg, name='Usereg')
]
