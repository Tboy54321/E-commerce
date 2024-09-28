from django.forms import ModelForm
from .models import Companies, Login, CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms

PASSWORD_ENTRY = 'Enter your password'
CONFIRM_PASSWORD_ENTRY = 'Confirm your password'

class CompanyForm(ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': PASSWORD_ENTRY}),
        # help_text=
        label='Password',
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': CONFIRM_PASSWORD_ENTRY}),
        label="Confirm Password"
    )
    class Meta:
        model = Companies
        fields = '__all__'

class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = "__all__"

class UserForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': PASSWORD_ENTRY}),
        help_text="Your password must be at least 8 characters long",
        label='Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': CONFIRM_PASSWORD_ENTRY}),
        help_text="Enter the same password as above",
        label="Confirm Password"
    )
    
    remember_me = forms.BooleanField(required=False, label='Remember Me')
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'role', 'phone_number']
        help_texts = {
            'email': None,
            'username': None,
        }
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email address'}),
            'username' : forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'phone_number': forms.NumberInput(attrs={'placeholder': 'Phone Number'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter last name'}),
        }

# Settings form for updating his profile like username, First name, middle name, Last name, profile pic, phone number
# Settings form will still inherit custom user model since it is the fields it needs in the form