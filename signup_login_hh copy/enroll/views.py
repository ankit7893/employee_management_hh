
import re
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm  
from .forms import SignupForm ,  EditUserProfileForm ,  EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm , UserChangeForm
from django.contrib.auth import authenticate, login, logout  , update_session_auth_hash

from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, 'enroll/index.html')


def sign_up(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)  
        if fm.is_valid():
            messages.success(request, 'accound registered successfully !!!!!!!!!!  ')
            fm.save()  
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
                    return HttpResponseRedirect('/profile') 
        else:
            fm = AuthenticationForm()  
        return render(request , 'enroll/user_login.html' , {'form':fm})
    else:
        return HttpResponseRedirect('/profile')




def profile(request):
    if request.user.is_authenticated: ## logiin 
        if request.method == "POST":
            if request.user.is_superuser == True:
                fm= EditAdminProfileForm(instance = request.user)
                users = User.objects.all()
            else:
                fm= EditUserProfileForm(request.POST , instance = request.user) 
                users = None
            if fm.is_valid():
                messages.success(request, 'Profile updated ')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm= EditAdminProfileForm(instance = request.user)
                users= User.objects.all() 
            else:
                fm= EditUserProfileForm(instance = request.user)
                users = None
            
        return render(request, 'enroll/profile.html' , {'name':request.user , 'form':fm , 'users':users})
    else:
        return render(request, 'enroll/profile.html')  


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/user_login')  



def user_change_pass(request):
    if request.method == "POST":
        fm=PasswordChangeForm(user=request.user , data=request.POST)
        if fm.is_valid():
            print("ndksfndsf")
            fm.save()   
            update_session_auth_hash(request, fm.user) 
            messages.success(request, 'password changed successfully ')
            return HttpResponseRedirect('/user_login') 
            
        else:
           

            return HttpResponse("wrong paSSWROD")
    else:
        fm= PasswordChangeForm(user=request.user)  
    return render(request, 'enroll/changepass.html', {'form':fm})




def user_detail(request,id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk = id)
        fm = EditAdminProfileForm(instance= pi)  
        return render(request, 'enroll/userdetail.html' , {'form':fm})
    else:
        return HttpResponseRedirect('/login/')
