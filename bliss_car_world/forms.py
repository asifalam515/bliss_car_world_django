from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from car.models import Comment
from django import forms
class RegisterForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['username','first_name','last_name','email']
class LoginForm(AuthenticationForm):
    pass
class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name',  'body']