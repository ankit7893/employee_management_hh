# copy the content of one file to amnther file 

# f= open("2.txt")
# f2 = open("new_one.txt","w")

# f2.write(f.read()) 

# f.close()
# f2.close()

#############################################

# number of lines starting with t 

# f= open("2.txt")

# for line in f:
#     if line[0]=="t":
#         print(line,end="")



# f= open("2.txt")
# c=0 
# l_lines = f.readlines()
# for line in l_lines:
#     if line[0]=="t" or line[0]=="T":
#         c=c+1
# print(c)

################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
# oops  
# definition , self , 
# methods >>> contructor special method , non-static method , static method, spacial method (dunder)
# variable  >>> static variable , instance variable , local variable 
# 
# 
# 
###############################################################################
###############################################################################
###############################################################################
###############################################################################



# -- object oreinted programming 
# -- it increase the reeadablity and efficiency of the code 
# -- methods -- functions that are created inside class 



# # class  , method , object 
# l=[10,20,30]    ##  
# l.append(40) 
# list.append(l,40)   
# print(l)

# # inbuilt classes - list , tuple , set , dict , string , float , int , range 


# syntaxes of classes

# contrauctor >>> 
# -- a special method that will used to initialize the object of the class
# -- it will be called automatically when object will be created 
# -- it will be always represented by __init__()

# -- self >> always represent the object of the class

# static method
# non - static method 

# contrucor

# class Students:
#     a = 0                                           ##    a = static 
#     def __init__(self,first_name,last_name,age=18):  # 
#         b=6 
#         Students.a += 1                           ##        
#         # print("contructor is running")
#         self.first_name  = first_name             ##  
#         self.last_name = last_name 
#         self.age=        age  
#         self.fullname  =  first_name + " " + last_name 
#         self.full_detail = first_name + " " + last_name + " " + str(age) 
        
#     # non - static method 
#     def show(self):
#         print(f"student first name  is {self.first_name}  and lastname is {self.last_name}  and age is {self.age} ")

#     # static method / class method 
#     def explain():
#         print(f" i have crreated the objects of student class {Students.a} ")  


    


# s1= Students("vishnu","roy",13)   ## ## object = s1 
# s2= Students("vatsal","garg",16)   ## ## object = s1 
# s3= Students("sriniwas","kumar")   ## ## object = s1 
# s4= Students("archna","sharma",20)   ## ## object = s1 
# Students.explain()  





# print(s1.full_detail) 

# s4.show()
# print(s4.last_name)
# print(s2.__dict__) 


################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################



# class Students:
#     a = 0                                           ##    a = static 
#     def __init__(self,first_name,last_name,age=18):  # 
#         b=6 
#         Students.a += 1                           ##        
#         # print("contructor is running")
#         self.first_name  = first_name             ##  
#         self.last_name = last_name 
#         self.age=        age  
#         self.fullname  =  first_name + " " + last_name 
#         self.full_detail = first_name + " " + last_name + " " + str(age) 
        
#     # non - static method 
#     def show(self):
#         print(f"student first name  is {self.first_name}  and lastname is {self.last_name}  and age is {self.age} ")

#     # static method / class method 
#     def explain():
#         print(f" i have crreated the objects of student class {Students.a} ")  

#     def __str__(self):
#         return (f" i am showing the string of obnject student first name  is {self.first_name}  and lastname is {self.last_name}  and age is {self.age} ") 

#     def __repr__(self):
#         return (f" i am  represnting the object of the class  ") 


# s1= Students("vishnu","roy",13)   ## ##  
# print(s1)  
# print(s1.__str__())  
# print(s1.__repr__())   ##  

# # str 
# # 

# # repr 


##############################################################################################
# inheritance 
# simple   >>> 1 parent  >> 1 child 
# multiple  >>> 2 parent  >> 1 chaild 
# hirerchical  >>>> 1 parent >>> 2 chaild
# multi-level  >>> 1 parent >>> child/parent  >>> child   (3 generations)

# class Phone:
#     def __init__(self,brand , ram , rom ):
#         self.brand  = brand 
#         self.ram = ram 
#         self.rom = rom 

#     def explain(self):
#         print(f"this phone is having brand  {self.brand} and  having ram {self.ram}  and rom {self.rom}   ")

# class Modern_phone(Phone):      #### 
#     def __init__(self, brand,rom , ram , b_camera , f_camera ):
#         super().__init__( brand,  ram , rom)
#         self.b_camera = b_camera  
#         self.f_camera = f_camera  

# class Future_phone(Modern_phone):  
#     def __init__(self, brand, rom, ram, b_camera, f_camera, transparency ):
#         super().__init__(brand, rom, ram, b_camera, f_camera) 
#         self.transparency =  transparency 


# F_P = Future_phone("jio", "500" , "20", "50" , "30" , "True")
# F_P.explain()  


# redmi = Modern_phone("redmi","128" ,"8", "20" ,"12") 
# redmi.explain()


# print(redmi.__dict__)

##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################


# polymorphism >> 
# when a same method can be applicable on many data types 
# this is called 
# -- eg len()



# poly >>>  many 
# morphism >> forms 

# len()  
# list , tuple , set , dict , string 



# sort  
# list 













######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################
# decorator >>  it will add some functionalty in function without changing the definition of the function  


# def dec(func):   ##    3     func= fun 
#     def wrap():  ### 
#         s= func()           ##        s= "helLo vIShnu"  
#         s=s.title()         ###         s=  "Hello Vishnu"
#         return s 
#     return wrap            ## 4 

# def fun():
#     return "helLo vIShnu"  

# fun  =  dec(fun)        ## fun

# print(  fun()  )  ###   1 


# # Hello Vishnu  



##############################################################


# def dec(fun_2):            ##  fun_2 =fun
#     def wrap(name): 
#         s= fun_2(name)          ### s= 
#         n_s = "welcome here \n" + s 
#         return n_s  
#     return wrap 

# def fun(name):
#     return "Hello " + name  

# fun = dec(fun)
 
# print(fun("vishnu"))  
################################################################






































