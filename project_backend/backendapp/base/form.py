from django.forms import ModelForm
from .models import Companies, Login

class RegForm(ModelForm):
    class Meta:
        model = Companies
        fields = '__all__'

class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = "__all__"