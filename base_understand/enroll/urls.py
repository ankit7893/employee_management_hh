
from django.urls import path
from enroll import views

urlpatterns = [
   
   path('', views.index), 
   path('about', views.about)
   
   
]


