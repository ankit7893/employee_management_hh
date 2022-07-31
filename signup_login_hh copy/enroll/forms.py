from tkinter import Label
from attr import field
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django import forms 


class SignupForm(UserCreationForm):
    password2 = forms.CharField(label="CONFIRM PASSWORD(AGAIN)  " , widget=forms.PasswordInput)
    class Meta:
        model = User 
        fields = ('first_name' , 'last_name','email','username')  
        labels = {'email': "EMAIL" , 'first_name': 'Enter first name  ', }  

    

class EditUserProfileForm(UserChangeForm):
    password = None 
    class Meta:
        model = User
        fields=  ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']
        labels = {'email': 'Email'}

class EditAdminProfileForm(UserChangeForm):
    password = None 
    class Meta:
        model = User
        fields=  '__all__'
        labels = {'email': 'Email'}
