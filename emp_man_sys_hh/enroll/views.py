from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render

from .models import Employee  

# Create your views here.

def index(request):
    return render(request , "index.html")    



def view_emp(request):
    emps = Employee.objects.all()    #### 
    return render(request, "view_emp.html" , {'emps':emps})


def add_emp(request):
    if request.method == "POST":   ### 
        name  = request.POST['name']    ##                 html >>>   
        age  = request.POST['age']  
        add   = request.POST['add']  
        sal  = request.POST['sal']   
        new_emp = Employee(name = name , age = age , add = add , sal = sal)
        new_emp.save()  
        return HttpResponse("new employee added successfully  <a href='http://127.0.0.1:8000'> go back </a> ")
    else:
        print("get method")
        return render(request, "add_emp.html")    



def remove_emp(request , emp_id=0):
    if emp_id:          # emp_id =3   
        try:
            emp_to_be_removed = Employee.objects.get(id = emp_id)  ##  
            emp_to_be_removed.delete() 
            return HttpResponse("employee removed successfully  <a href='http://127.0.0.1:8000'> go back </a>  ")   
        except:
            return HttpResponse("please enter a valid emp id ")   
    emps = Employee.objects.all()   ###  
    # return render(request,  'remove_emp.html' , {'emps':emps})
    return HttpResponseRedirect()



def filter_emp(request):  ##
    if request.method == "POST":     ##  True 
        name  = request.POST["name"]      #      name = "s"             #      name = "a"   
        add  = request.POST["add"]      ## add = ""
           
        emps  = Employee.objects.all()   ###  
        if name:         ###           "s"  
            emps  = emps.filter(name__icontains = name )    # chris.__icontains = "s" 
        if add :
            emps = emps.filter(add__icontains = add )    

        return render(request, "view_emp.html" ,{'emps':emps})  


    return render(request , "filter_emp.html")  ##


