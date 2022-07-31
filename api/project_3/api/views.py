
from functools import partial
from pprint import pformat
from django.http import HttpResponse
from django.shortcuts import render
import io 
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def student_api(request):
    if request.method== "GET": ##  
        json_data = request.body 
        stream  = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)  ## {'id':4} 
        print(python_data)
        id = python_data.get('id', None)   ## id = 4
        print("id", id)   
        if id is not None:
            stu = Student.objects.get(id=id)  ### 
            serializer  = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type= 'application/json')
        else:
            stu = Student.objects.all()  ### 
            serializer  = StudentSerializer(stu, many =True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type= 'application/json')
            
    if request.method == "POST":
        json_data = request.body      ###  
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)       ## 
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()        
            res = {'msg':"data added successfuly "}  ### 
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')

    if request.method == "PUT":
        json_data = request.body      ###  
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)  
        id  = python_data.get('id')   #### 
        print(id)
        stu = Student.objects.get(id=id)   
        serializer = StudentSerializer(stu, data=python_data)
        if serializer.is_valid():
            serializer.save()        
            res = {'msg':"data updated  successfuly "}  ### 
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
   
    if request.method == "PATCH":
        json_data = request.body      ###  
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)  
        id  = python_data.get('id')   #### 
        print(id)
        stu = Student.objects.get(id=id)   
        serializer = StudentSerializer(stu, data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()        
            res = {'msg':"data updated partailly and   successfuly "}  ### 
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
   

    if request.method == "DELETE":
        json_data = request.body  
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream) 
        id  = python_data.get('id')   #### 
        stu = Student.objects.get(id=id) 
        stu.delete()
        res = {'msg':"data deleted successfuly "}  ### 
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type = 'application/json')





