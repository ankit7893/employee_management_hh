import re
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm  
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login, logout  , update_session_auth_hash

from django.contrib.auth.models import Group, User
# Create your views here

def index(request):
    return render(request, 'enroll/index.html')


def sign_up(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)  
        if fm.is_valid():
            messages.success(request, 'accound registered successfully !!!!!!!!!!  ')
            user = fm.save()  
            group = Group.objects.get(name='editor')
            user.groups.add(group)
        else:
            return HttpResponse(" data is not valid ")

        fm = SignupForm()    ### 
        return render(request , 'enroll/sign_up.html' , {'form':fm}) 
        
    else:
        fm = SignupForm()  
    return render(request , 'enroll/sign_up.html' , {'form':fm})
    


def user_login(request):
    if not request.user.is_authenticated: ## if user is not loggin   >>> True 
        if request.method == "POST":
            fm = AuthenticationForm(request=request,data=request.POST)  
            if fm.is_valid():           ### 
                uname = fm.cleaned_data['username']    ### username 
                upass = fm.cleaned_data['password']
                user  = authenticate(username = uname , password = upass)  
                if user is not None: 
                    login(request, user)  
                    messages.success(request, ' loggin successfully !!!!!!!!!!  ') 
                    return HttpResponseRedirect('/dashboard') 
        else:
            fm = AuthenticationForm()  
        return render(request , 'enroll/user_login.html' , {'form':fm})
    else:
        return HttpResponseRedirect('/dashboard')




def dashboard(request):
    if request.user.is_authenticated: ## logiin 

        return render(request, 'enroll/dashboard.html' , {'name':request.user.username})
    else:
        return render(request, 'enroll/dashboard.html')  


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/user_login')  




