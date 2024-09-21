from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Companies(models.Model):

    INDUSTRY_CHOICES = {
        ('automoobile', 'Automobile'),
        ('spare parts', 'Spare Parts'),
        ('services', 'Services'),
    }

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    industry_type = models.CharField(max_length=255, choices=INDUSTRY_CHOICES)
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

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'Admin'),
        ('company', 'Company')
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    roles = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.username
    
