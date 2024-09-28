from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.

class Companies(models.Model):
    # profile_pic = models.ImageField()
    name = models.CharField(max_length=255, null=False)
    # registration_number = 
    # company_type = 
    email = models.EmailField(unique=True, max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    confirm_password = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=True)
    opening_hours = models.CharField(max_length=50)
    address = models.TextField(null=False)
    phone_number = models.IntegerField(unique=True, null=False)
    # industry_type = models.CharField(max_length=255, choices=INDUSTRY_CHOICES)
    website = models.URLField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
class Login(models.Model):
    
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.password

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('company', 'Company')
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    phone_number = models.IntegerField(unique=True, null=True)
    # profile_pic = models.ImageField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.username

# USE ORM