from django.forms import ModelForm
from .models import Companies, Login, CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegForm(ModelForm):
    class Meta:
        model = Companies
        fields = '__all__'

class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = "__all__"

class UserForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        help_text="Your password must be at least 8 characters long"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
        help_text="Enter the same password as above"
    )
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password1', 'password2', 'role']
        help_texts = {
            'email': None,
            'username': None,
        }
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email address'}),
            'username' : forms.TextInput(attrs={'placeholder': 'Enter your username'}),
        }