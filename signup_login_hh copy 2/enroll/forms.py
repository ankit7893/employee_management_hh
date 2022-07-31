from tkinter import Label
from attr import field
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from django import forms 


class SignupForm(UserCreationForm):
    password2 = forms.CharField(label="CONFIRM PASSWORD(AGAIN)  " , widget=forms.PasswordInput)
    class Meta:
        model = User 
        fields = ('first_name' , 'last_name','email','username')  
        labels = {'email': "EMAIL" , 'first_name': 'Enter first name  ', }  

    

