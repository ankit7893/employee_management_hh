from django.http import HttpResponse
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser  
from .serializer import StudentSerializer

from rest_framework.renderers import JSONRenderer  
from django.views.decorators.csrf import csrf_exempt 
@csrf_exempt  
def student_create(request):
    if request.method  == "POST":
        json_data =request.body  ## 
        stream = io.BytesIO(json_data)  
        print("stream is  >>> " , stream)
        python_data = JSONParser().parse(stream)  ## 
        print("python data is", python_data)
        serializer = StudentSerializer(data=python_data)
        print("serializer data is >>> ", serializer )
        if serializer.is_valid(): ## 
            print("valid")
            serializer.save()
            res = {'msg': 'data created'}  
            json_data = JSONRenderer().render() 
            return HttpResponse(json_data, content_type= 'application/json')
        else:
            print("not valid")
            json_data = JSONRenderer().render(serializer.errors) 
            return HttpResponse(json_data, content_type= 'application/json')








