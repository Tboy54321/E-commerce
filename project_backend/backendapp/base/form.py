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
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))
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