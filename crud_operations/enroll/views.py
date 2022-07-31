import email
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect

from enroll.models import User
from .forms import StudentRegistration
# Create your views here.


def addandshow(request):
    if request.method == "POST":                      ## True 
        fm = StudentRegistration(request.POST)        ### 
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name= nm , email=em , password = pw)   
            reg.save()    
            fm= StudentRegistration() 
            stu= User.objects.all() 
    else:
        fm= StudentRegistration()   
        stu= User.objects.all()         ##  stu=None 
    return render(request , 'enroll/addandshow.html' , {'form':fm , 'stu':stu})



def update_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm= StudentRegistration(request.POST, instance=pi)  
        if fm.is_valid():
            fm.save()  
    else:
        pi = User.objects.get(pk=id)
        fm= StudentRegistration() 
        # fm= StudentRegistration(instance=pi) 
    return render(request, 'enroll/updatestudent.html' , {'id':id, "form":fm})






def delete_data(request, id):  ## id=60 
    if request.method == "POST":          ## 
        pi = User.objects.get(pk=id)           ### pk= 60 
        pi.delete()
        return HttpResponseRedirect('/')
        return HttpResponse("record got deleted ")

