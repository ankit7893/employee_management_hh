## >>> what is django 
# -- python web framework 
# -- it is very extensive means having huge in-built configurations 
# -- rapid development 
# -- django follows MVT achiutecture 


#######################################################################
# django vs flask 
# django gives the fast development as compared to flask 
# It is desirable to use django for big projects as compared to flask. 
# flask use MVC and django use MVT
########################################################################

# MVT 
# controller 
#############################################
# >>> explain django archiutecture 
# -- it follows MVT (model view template architecture)
# -- django itself works like a controller 

# #########################################################

# when we open a URL in broser a request has been sent to the server
# and server will decide which HTMl content has to be response corresponding to
# that URL
########################################################################
# MVT 

# user request >>> django(controller) >>>> URL >>> views >>> templates >>> models 

############################################################################
# module vs package 

# module >>> simple python file having python objects and functions 

# package >>> -- a directiry/folder having collection of modules  
#             -- present of init  file there represent it is a package 
#             -- init file can be empty or not empty 
#########################################################################
# app  vs project

# eg.  payment gateway(app) in amazon(project)
# -- A project will be bundle of apps
#####################################################################
# phases >>> development >>> deployment  >>>  prodcution 
#
# development  >>> creating the website        |||   debug - True 
# deployment   >>> launching the website 
# production   >>> when it is launched already ||| debug - False 

######################################################################
# model file >>> it will handle the db ||| create , delete , edit the db 
# template  >>>  Html files ||| it wwill represent the webpage
########################################################
# view   file  >>> in this file all business logic we will  
# write and this file will get the request and it will render template after 
# adding the data from the models file as a response 
#########################################################
# admin file >>>  this file will be used for registering the tables created in the models
# to the db 
#################################################################
# manage.py >>> it will helps in interacting with apps and projects 
###########################################################
# urls >>> file will have all urls connectivity 
########################################################
# explaiun the request flow in Django 

# request(url) >>>><<<<  manage.py >>><<<  settings.py file >>><<<  urls >>><<<  views >>> templates and model 
###########################################################
# get vs post 

# when web page will give some data from user >>> POST 
# 

##############################################################
# csrf_token >>>   
# cross site request forgery 
###############################################################  








######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
# commands 
# pip install django 
# python -m django --version 
# django-admin startproject projectname
# python manage.py runserver
# python manage.py startapp appname 
# python manage.py makemigrations    ### 
# python manage.py migrate    
# python manage.py createsuperuser      




############################################################################
# create the project || app || connect them 
# check the server
# index logic in views file 


#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################d
# exception handling 

# try >> errror >> except block will execute 
# try >> no error >>> else block will execute 

# try :
#     print(9/3) 
#     n=int(input("enter n: "))  ##  45
    
# except ZeroDivisionError:
#     print("please dont devide by zero ")

# except ValueError: 
#     print("please enter interger input only ")

# except:
#     print("something else went wrong")

# else:
#     print("everything is fine") 

# finally:
#     print("finished")
























