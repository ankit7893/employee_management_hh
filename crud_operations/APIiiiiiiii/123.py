# api 
# aplication programming interface 

# 

#
# web api 
# ###############################
# how it works
# 1.
# 2. 
# 3. 
# 4. 

##################################################

# REST api 
###################################################
#       op         http methods
# C -  create  --  POST 
# R -   REad -     GET
# U -   UPDATE  --  PUT , PATCH (put- complete update , patch- partial update )
# D -   delete  --  DELETE 
##################################################################

# http://google.com/api/map
#################################################################

# REQUEST                                   Response 
# GET:/api/student                         {'id':1 , 'name':"rahul" , 'id':2 , 'name':"riya" ,}
# GET:/api/student/1                      {'id':1 , 'name':"rahul"}  

# POST:/api/student                        {'id':3 , 'name':'sumit'}
# {"name":'sumit'}  

# PUT:/api/student/1                         {'id':1 , 'name':'raj"}
# {"name":'raj'} 

# DELETE:/api/student/1                        {'id':1 , 'name':'raj"} 

# id >> put and delete  (neceesary)
# id >> get  (optional)
# id >> POST  (no need)
# 
#################################################
# DRF 
# 1. fullform
# 2. 
# 3. 
# 4. 
# 5. 
# 6.  'rest_framework'

#################################################################################
# JSON 
# 1. full form 
# 2. dumps >>>> python objects >>> json strings
# 3. loads >>>  json string >>>  python objects (parsing)


# import json 

# d= {'name':"ankit", "rol":101, "age": """244444"""}

# d = json.dumps(d)

# print(d)
# print(type(d))

################################################################### 
# import json
# j_s= '{"name": "ankit", "rol": 101, "age": "244444"}'

# p_d= json.loads(j_s)
# print(p_d)
# print(type(p_d)) 
###############################################################################
#                              serialization >>>   
# model instance / queryset   >>>>>>>>>>>>>>>>>   python datatypes 

###########################################################################  
















