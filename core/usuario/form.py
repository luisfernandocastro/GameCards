from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

class LoginForm (AuthenticationForm):
    def __init__(self, *args,**kwargs):
        super(LoginForm,self).__init__(*args,**kwargs)
        self.fields['username']
        self.fields['password']



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields= ("username","password1", "password2")
    