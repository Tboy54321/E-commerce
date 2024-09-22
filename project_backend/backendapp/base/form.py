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
            'password1': None,
            'password2': None,
        }
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Enter email address'}),
            'username' : forms.TextInput(attrs={'placeholder': 'Enter your username'}),
        }
    
    # def clean_password2(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')

    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords do not match.")

    #     # Custom validation for minimum length
    #     if len(password1) < 8:
    #         raise forms.ValidationError("Password must be at least 8 characters long.")
        
    #     return password2