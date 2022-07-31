
from django.http import HttpResponse
from django.shortcuts import render , HttpResponseRedirect
from .forms import Sign_up_form 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.models import User

# Create your views here.

def sign_up(request):
    if request.method == "POST":
        fm = Sign_up_form(request.POST)   
        if fm.is_valid():
            messages.success(request, 'account rreated successfully  ')
            fm.save()  
            fm = Sign_up_form()  
            return render(request, 'enroll/sign_up.html' , {'form':fm}) 
        else:
            messages.error(request, "data is not valid")  
        return render(request, 'enroll/sign_up.html' , {'form':fm}) 
    
    else:
        fm = Sign_up_form() 
        return render(request, 'enroll/sign_up.html' , {'form':fm})     






def user_login(request):
    if not request.user.is_authenticated:   ## 
        if request.method == "POST":
            fm= AuthenticationForm(request = request , data =request.POST)
            if fm.is_valid():
                global uname
                uname = fm.cleaned_data['username']  
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname , password = upass )
                if user is not None:
                    login(request, user)
                    messages.success(request, 'logged in successful ')  
                    return HttpResponseRedirect('/profile/' , {'name': uname})
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/user_login.html',{'form':fm})

    else:
        return HttpResponseRedirect('/profile/')
 

def user_profile(request):
    # user = User.objects.get(username=username)
    return render(request, 'enroll/profile.html')



def user_logout(request):
    logout(request)
    # return HttpResponse("ankhfds")
    return HttpResponseRedirect('/user_login/')

