
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 

from django import forms 


class Sign_up_form(UserCreationForm):
    password2 = forms.CharField(label='confirm password (again) : ' , widget=forms.PasswordInput) 
    email = forms.EmailField(required=True)   
    first_name = forms.CharField(required=True)  
    last_name = forms.CharField(required=True)  

    class Meta :
        model = User 
        fields = ['username','first_name' , 'last_name', 'email']
        labels = {'email' : 'Email'} 
        



