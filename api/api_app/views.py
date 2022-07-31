
from traceback import print_tb
from django.shortcuts import render


from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

def Student_detail(request,pk): ### 
    stu = Student.objects.get(id=pk)   ###
    print()
    print("stu is>>>> " ,  stu, type(stu))
    serializer = StudentSerializer(stu)   ### 
    print()
    print("serializer is  >>>> " , serializer, type(serializer))
    json_data = JSONRenderer().render(serializer.data)  
    print()
    print("josn >>>> " , json_data, type(json_data))
    return HttpResponse(json_data, content_type = 'application/json')



def student_list(request):
    stu = Student.objects.all()  
    serializer = StudentSerializer(stu , many=True) 
    json_data = JSONRenderer().render(serializer.data)  
    return HttpResponse(json_data, content_type = 'application/json')


