


# # # ========================================================================================================
# # # ========================================================================================================
# # # ========================================================================================================
# # # ========================================================================================================
# # # ========================================================================================================
# # # ========================================================================================================
# # # ========================================================================================================
# # # ========================================================================================================
# # # ========================================================================================================
# # # ========================================================================================================
# # # ========================================================================================================
# # # ========================================================================================================
# # # ========================================================================================================
# # # ========================================================================================================
# # # ========================================================================================================
# # # ========================================================================================================
# # # ========================================================================================================
# # # ========================================================================================================
# # # ========================================================================================================
# # # ========================================================================================================
# # # ========================================================================================================
# why oops??????                                                 #        object oriented programmings... 



# # # it makess programs more readable and efficient.     


# # function  >>>>  a  code of block which can perform a perticular task and can be used several times.. 
                                      
                                                                                                           
# # # methods are functions which are defined under the class.                                                                                 

# # # class, object , instances, method                           (function in class)      
                                                                                            
# # # # ===========================================================   
# class , method , object 
                                          
# l=[1,2,3]                               # class/structure    ,,,    object>>   ,,,,,   method                                                                                                                                                        
# # l.append(8)                             #                                                                                                                                           
# list.append(l,8)                                                                                                                                                                                                      
# print(l)                                                                                                                    

# 

# # # ==========================================================                                                       



# # # =========================================================================  
# # # list is a class...                               
# # # # l=[]             object of list 

# # # list class...                                    #append  is a method....                  
# # # list object
# # # method 
# # # =========================================================================

# # constructor >>> constructor is a special method which is used to initailised the object of the class. 
# # constructor >>>>> will be called automatically when object of the class will be created 
# # constructor  >>>> it will always be represented as __init__() 

#  self will be representing the object of the class

# # list  ,  tuple  , dict  , set ,  

# class Students:                                                # convention/trend     vs  rule                               
#     def __init__(self, first_name , last_name, age):              # we can write anything in place of self    
#         # print("contructor running")     
#         self.first_name=first_name        ### s1.f_name = "ankit"            # instances  # p1.firstname = ankit
#         self.last_name=last_name 
#         self.age= age            
    
# s1=Students('ankit', 'dhiman',15)           # s1 = {firstname: ankit  ,  lastname: dhiman ,   age : 15 }
# s2=Students('sahil', 'khan',25)       
# s3=Students('akash', 'saini',27)    
# s4=Students('aman', 'saini',26)    
# s5=Students('rahul', 'roy',29)    
# print(s1)
# print(s2.__dict__) 
# print(s4.__dict__)
# print(s2.last_name)




# class || contructor || self || objects || method || instances || 


# class School:
#     a=24
#     def __init__ (self, first_name, last_name, age):
#       self.first_name=first_name
#       self.last_name= last_name
#       self.age=age    
      
#     def full_name(self):
#       return f"hi my firstname {self.first_name} and my last name {self.last_name} and my age is {self.age}"

# s1=School("ankit","dhiman",25)
# s2=School("moon","stars",23)
# s3=School("India","America",24)  
# print(s1.full_name())
# print(s3.age)
# print(s2.__dict__)
# print(s1)

# print()


























# class Friends:
#     def __init__(self,firstname,lastname,phone_number=897543):
#         self.firstname=firstname
#         self.lastname=lastname
#         self.phone_number=phone_number


# f1=Friends("jenny","goldman")
# f2=Friends("neetu","singh",11111)
# print(f1.lastname)
           
# print(f2.__dict__)  






# # # print(p2.__dict__)  
                                
# # # print(p2.age)                                          






# # # p2= Person('sahil','khan',19)                          
# # # print(p2.first_name)                  







# # # # # # =============================================================================
# class Laptop:
#     def __init__(self, brand ,model_name , price=100):
#         self.brand=  brand                                               #laptop1.brand= "hp"
#         self.name = model_name
#         self.price=price  
#         self.laptop_name = brand + " "  + model_name 
#         self.full_detail= brand+ " "+ model_name + " " + str(price)           

# laptop1=Laptop("hp","au114tx")                                                  #1
# # print(laptop1.laptop_name)              
# # print(laptop1.full_detail)              

# laptop2=Laptop("lenovo","ax",63000)                                            #1
# # print(laptop2.laptop_name)    
# # print(laptop2.full_detail)   
# print(laptop1.__dict__)      


# # # ===================================================================================
# # # intance method              class = list ,  object = l    ,  method =pop
# l=[1,2,3]        
# l.pop()                        
# print(l)         

# # # # # # ==============================================================
# class Person:
#     def __init__(self,first_name, last_name, age):
#         self.first_name= first_name
#         self.last_name= last_name
#         self.age=age   

#     def full_name(self): 
#         return    f" firstname is  {self.first_name} and lastname is  {self.last_name}   "                          #   "ankit{} dhiman".format("ankit")"          #   f"ankit dhiman"

# p1=Person("ankit", "dhiman", 24)                   #p1= .............      ..............      ........ 
# p2=Person('sahil', 'khan',19)                 #  .............       ........ 

# print(p1.full_name())                            # call                 
# print(Person.full_name(p1))                    # same 


# # # ===============================================================
# # # ===============================================================

# # 1. what is classs
# # 2.what is object 

# # 3. what is the use of self in the classes
# # 4. what is method
# # 5. create a student class and make 10 objects of the class...  they should accecible by the object of the class
# # 6. what is constructor ..

# # # ===============================================================
# # # ===============================================================
# # # ===============================================================
# # # ===============================================================
# # # ===============================================================
# # # ===============================================================
# # # ===============================================================
# # # ===============================================================


# # # =================================================================

# class Person:
#     def __init__(self,first_name, last_name, age):      
#         print("aniket")     
#         self.first_name= first_name
#         self.last_name= last_name   
#         self.age=age                        
    
#     def full_name(self):                       
#         return f"{self.first_name} {self.last_name}"                                                        

#     def is_above_18(self):
#         return self.age>18               

# p1=Person("ankit", "dhiman", 20)                 #p1=....... ...............        .       ..............    p2= ......... ....... ....... 
# p2=Person('sahil', 'khan',19)  
# p3=Person('rahul', 'khan',13)  
# p4=Person('ajay', 'khan',21)  

# print(p3.is_above_18())               
# print(p2.full_name())
# print(Person.full_name(p2))          

# # # ======================================================================


# 


# class Laptop:
#     def __init__(self, brand ,model_name ,  price):     
#         self.brand=brand
#         self.name = model_name
#         self.price=price
#         self.laptop_name = brand + " " + model_name 

#     def apply_dicount(self,num):                          # num=10
#         off_price= (num/100)*self.price   # =  (10/100)*2300=  230.0   
#         return self.price-off_price             # 2300  - 230.0 = 2070.0    

# laptop1=Laptop("hp","au114tx",6000)     
# laptop2= Laptop('apple','mac',2400)  
# print(laptop2.apply_dicount(50))               


# # # print(Laptop.apply_dicount(laptop2,50))  
# # # ==========================================================================
# # # # class variable
# # # write a program using class of circle that will give output as
# # #  circumfereence  of circle we are just passing radius.    
# # # pi=3.14                   # global var



# class Circle:   
#     pi=3.14              # class var               
#     def __init__(self,radius):                   #2
#         print("a")                                #3
#         self.radius=radius                       #4                     

#     def cal(self):                  
#       return  2* Circle.pi *self.radius                    #7  
        
# c=Circle(5)                                       #1
# print(c.cal())                                    #5



# # # ====================================================
# # #  write a program by using class of laptop that recieving detail of laptop and need 
# # # # to give 10 % on each laptop

# class Laptop:
#     dc=10  
#     def __init__(self, brand ,model_name ,  price):
#         self.brand=brand
#         self.name = model_name
#         self.price=price
#         self.laptop_name = brand + " "  + model_name    

#     def apply_dicount(self):
#         off_price= int((Laptop.dc/100)*self.price)                                        # /  flost= 1.0                     // int= 1
#         return self.price-off_price                     


# laptop1=Laptop("hp","au114tx",600)    
# laptop2= Laptop('apple','mac',100)        
# print(laptop1.apply_dicount())             


# # # # # # # # ==========================================================
# class Laptop:              
#     discount_percent=50                                         #
#     def __init__(self, brand ,model_name ,  price):
#         self.brand=brand
#         self.name = model_name
#         self.price=price
#         self.laptop_name = brand + " "  + model_name 

#     def apply_dicount(self):
#         off_price= (Laptop.discount_percent/100)*self.price              #  /      //
#         return self.price - off_price  
 
# laptop1=Laptop("hp","au114tx",600) 
# laptop2=Laptop("lenovo","g580",23000)    
# print(laptop1.__dict__)    
# print(laptop1.apply_dicount())          
# Laptop.discount_percent=100                                                     
# print(laptop1.apply_dicount())                                
# print(laptop2.apply_dicount())                               


 
# # # ================================================================
# # # # # # l2 discount
# class Laptop:
#     discount_percent=10        ###       
#     def __init__(self, brand ,model_name ,  price):
#         self.brand=brand
#         self.name = model_name
#         self.price=price
#         self.laptop_name = brand + " "  + model_name 

#     def apply_dicount(self):
#         off_price= (self.discount_percent/100)*self.price
#         # off_price= (Laptop.discount_percent/100)*self.price
#         return self.price-off_price


# laptop1=Laptop("hp","au114tx",1000)    
# print(laptop1.apply_dicount())    
# laptop1.discount_percent=50     
# print(laptop1.apply_dicount()) 

# laptop2= Laptop('apple','mac',1000)     
# print(laptop2.apply_dicount())     



# # # ===========================================================

# class Person:
#     a = 0  

#     def __init__(self,first_name, last_name, age):       #2
#         Person.a+=1                                        #3
#         self.first_name= first_name               #4
#         self.last_name= last_name                 #5
#         self.age=age                            #6


# p1=Person("ankit", "dhiman", 10)                                            #1
# p1=Person("ankit", "dhiman", 10)                                            #1
# p1=Person("ankit", "dhiman", 10)                                            #1
# p1=Person("ankit", "dhiman", 10)                                            #1
# p1=Person("ankit", "dhiman", 10)                                            #1
# p1=Person("ankit", "dhiman", 10)                                            #1
# p1=Person("ankit", "dhiman", 10)                                            #1

# print(Person.a)                                                             # 

# # # # ==========================================================================
# # # # ==========================================================================
# # # # ==========================================================================
# # # # ==========================================================================

# 11  feb     2021 



# # # class method         vs                                              intance mthod
# class Person:
#     count_instance=0                                                  #class variable   def
#     def __init__(self,first_name, last_name, age):
#         Person.count_instance+=1 
#         self.first_name= first_name
#         self.last_name= last_name
#         self.age=age                 
    
#     def hello():
#         return "hello , how are you"

#     def full_name(self):               
#         return f"{self.first_name} {self.last_name}"    

#     def is_above_18(self):         
#         return self.age>18  
# p1=Person("ankit", "dhiman", 10)                                            #1
# p2=Person('sahil', 'khan',19)                      
# p2=Person('sahil', 'khan',19)                            
# p2=Person('sahil', 'khan',19)                      
# p2=Person('sahil', 'khan',19)   
# print(p1.is_above_18())    

# print(Person.count_instances())    

# print(Person.hello())  


# # # ============================================================================



# # # 24-4-20  sachin
# # # =====================================================
# # # class method as constructor 
# class Person:
#     count_instance=0       #class variable
#     def __init__(self,first_name, last_name, age):
#         print("a")    
#         Person.count_instance+=1
#         self.first_name= first_name
#         self.last_name= last_name
#         self.age=age      



#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"          

#     def is_above_18(self):
#         return self.age>18
# p3=Person.from_string('ankit,dhiman,41')           #  p3=Person("ankit", "dhiman", "41")   
# print(p3.full_name())    
# # # # # ==========================================================================


# # # static method

# # class Person:
# #     count_instance=0       #class variable
# #     def __init__(self,first_name, last_name, age):
# #         Person.count_instance+=1
# #         self.first_name= first_name
# #         self.last_name= last_name
# #         self.age=age

# #     @classmethod
# #     def from_string(cls,string):
# #         first, last,age=string.split(',')
# #         return cls(first,last, age)
    
# #     @classmethod
# #     def count_instances(cls):
# #         return f"you have created {cls.count_instance} of {cls.__name__} class"

# #     @staticmethod
# #     def hello():
# #         print("hello status")                       

# #     def full_name(self):
# #         return f"{self.first_name} {self.last_name}"

# #     def is_above_18(self):
# #         return self.age>18

# # p1=Person("ankit", "dhiman", 10)      
# # p2=Person('sahil', 'khan',19)
# # Person.hello()                      
# # # # ===================================================================================================

# # # encapsulation   (putting the instances and methods(working on instances of class) all together)             
# # # abstraction     (hiding the complexity of methods in class) (complexity hiding)     (encapsulation > abstraction) 

# # # price            _price                __price   
# # # public  ,,,     protected  ,,,,,,       private             

# class Phone:
#     def __init__(self, brand, model_name , price):                       # 
#         self.brand= brand                                               #_price                price    
#         self.model_name = model_name                                               
#         self.__price=price                                                 #convension for private name

#     def full_name(self):                                          
#         return f"{self.brand}{self.model_name} {self.__price}"  

#     def hello():
#         return "hello , how are you"


                                                                         
#     def make_a_call(self,phone_number):                                                
#         print(f"calling{phone_number} ...")                                       
    
        
# phone1=Phone('nokia',"1100",1000)   
# print(phone1._Phone__price)
# # print(phone1.__dict__) 
# # print(phone1.__price)                                                                



# # # =========================================================================


# # # l=[4,1,6] 
# # # l.sort()            #sort()                 # bubble sort method               # tim sort method
# # # print(l)



# # # ====================================================================================================================
# # # ==============================================================================================================
# # # ================================================================================================================

# # # =======================================================================
# # # __name__ # dunder, magic methods                      (not a convenstion )  __price
# # # =============================================================


# # # __price          >>>>>>>   i was not permitted to print it outside of the class 

# # #  __price    >>>>>>>   if you really want to use it outside of the class then you should be taking 
# # # # the permission from the class.............     phone1._Phone__price     

# price >>  public 
# _price >>  protected
# __price >>  private


# class Phone:
#     def __init__(self,brand,model_name , price):
#         self.brand=brand
#         self.model_name =model_name
#         self.__price=price                                        # rule for change 

#     def make_a_call(self,phone_number):
#         print(f"calling{phone_number} ...")                    

#     def full_name(self):
#         return f"{self.brand}{self.model_name}"           

# phone1=Phone('noika',"1100",1000)   
# print(phone1._Phone__price)                                   #1000    
# # print(phone1.__dict__) 
# phone1._Phone__price=-1000                               # _Phone__price  = -1000      
# print(phone1._Phone__price)                               #-1000



# # # print(phone1.__dict__)          
# # # # ===================================================================



          
# # # =============================================================================

# # # # inheritance                         

# # # # single inheritence    # 1 parent >>> 1 child               

# # # # multilevel (grand parend(3 gen ))  , # 1 g pa>>>  child/parent >>>child      
# # # #   
# # # # multiple(multi- parent) ------    2 parent  >>   1 child     

# # # # hierarchical---    1 parent >>>>> 2 child       
# # # # =====================================================


# # 
# # 

# class Phone:                                               #      parent       (3 proper)       
#     def __init__(self,brand,model_name , price):     
#         self.brand=brand
#         self.model_name =model_name
#         self._price=max(price,0)         #     (-100,0)
#     def full_name(self):
#         print("i am here")
#         # return f"{self.brand}{self.model_name}"   
#     def make_a_call(self,phone_number):
#         self.full_name() 
#         print(f"calling{phone_number} ...") 

# class Smartphone(Phone):                                                                 
#     def __init__(self,brand,model_name , price, ram, internal_memory , rear_camera):   #  6  property
#         # Phone.__init__(self,brand, model_name,price)                #1 uncommon
#         super().__init__(brand, model_name,price)                     #2 common
#         self.ram=ram  
#         self.internal_memory=internal_memory 
#         self.rear_camera=rear_camera   

#     def make_a_call(self,phone_number): 
#         print(f"calling{phone_number} ...")     

# phone=Phone("noika","1100",-100)                   # 
# phone.make_a_call("123456765432")  
# smartphone= Smartphone("oneplus","5",300000,"6 gb","64 gb","20 mp")    # 
# print(smartphone.full_name())  



# # # ===================================================================================================
# # # # heirarchical    

# class Phone:                                                                 
#     def __init__(self,brand,model_name , price):
#         self.brand=brand
#         self.model_name =model_name
#         self._price=max(price,0) 

#     def full_name(self):
#         return f"{self.brand}{self.model_name}"   
#     def make_a_call(self,phone_number):
#         print(f"calling{phone_number} ...")                             

# class Smartphone(Phone):                                                                 
#     def __init__(self,brand,model_name , price, ram, internal_memory , rear_camera):
#         # Phone.__init__(self,brand, model_name,price)                 #1 uncommon
#         super().__init__(brand, model_name,price)  
#         self.ram=ram  
#         self.internal_memory=internal_memory
#         self.rear_camera=rear_camera
#     # def full_name(self):
#     #     return f"{self.brand}{self.model_name}"
#     def make_a_call(self,phone_number):          
#         print(f"calling{phone_number} ...") 

# class Smartphone2(Phone):                                                                 
#     def __init__(self,brand,model_name , price, ram, internal_memory , rear_camera):
#         # Phone.__init__(self,brand, model_name,price)                 #1 uncommon
#         super().__init__(brand, model_name,price)
#         self.ram=ram  
#         self.internal_memory=internal_memory 
#         self.rear_camera=rear_camera 
#     def full_name(self):
#         return f"{self.brand}{self.model_name}"
#     def make_a_call(self,phone_number):
#         print(f"calling{phone_number} ...")     

# phone=Phone("noika","1100",1000)   
# new= Smartphone("oneplus","5",300000,"6 gb","64 gb","20 mp") 
# new1= Smartphone2("oneplus","5",300000,"6 gb","64 gb","20 mp") 
# print(new1.full_name()+new.full_name())     

# # # ===================================================================================


# # # multilevel inheritance             (1 parent...  1 child/parent ...   1 child) 


# class Phone:                                                                 
#     def __init__(self,brand,model_name , price):           #3
#         self.brand=brand
#         self.model_name =model_name
#         self._price=max(price,0)
#     def full_name(self):
#         return f"{self.brand}{self.model_name}"      
#     def make_a_call(self,phone_number):
#         print(f"calling{phone_number} ...")   

# class Smartphone(Phone):                                                                 
#     def __init__(self,brand,model_name , price, ram, internal_memory , rear_camera):                # 6        
#         # Phone.__init__(self,brand, model_name,price)                 #1 uncommon
#         super().__init__(brand, model_name,price)      
#         self.ram=ram  
#         self.internal_memory=internal_memory
#         self.rear_camera=rear_camera
#     # def full_name(self):
#     #     return f"{self.brand}{self.model_name}"  
#     def make_a_call(self,phone_number):
#         print(f"calling{phone_number} ...")

# class FlagshipPhone(Smartphone): 
#     def __init__(self,brand,model_name , price, ram, internal_memory , rear_camera, front_camera):          #7

#         super().__init__(brand,model_name , price, ram, internal_memory , rear_camera)

#         self.front_camera=front_camera 

# phone=Phone("noika","1100",1000)  
# smartphone= Smartphone("oneplus","5",300000,"6 gb","64 gb","20 mp")    #2
# oneplus= FlagshipPhone("oneplus","5",300000,"6 gb","64 gb","20 mp", "16 mp")     #3

# print(oneplus.full_name())    

# # # =====================================================================

# print(isinstance([3,4],list))                 

# print(isinstance([3,4],tuple))                           
# # # =========================================================================





 

# class A:
#     def class_a_method(self):
#         return "A"
#     def hello(self):
#         return "hello from A"  

# class B:
#     def class_b_method(self):
#         return "B"
#     def hello(self):
#         return "helllo from B"                   

# class C(A,B):                             
#     pass 

# c1=C()               
# print(c1.hello())    
# print(C.mro())     
# Method Resolution Order (MRO) 
# print(c1.class_a_method())       
# print(c1.class_b_method())                 
# print(C.__mro__)  

# # # ===========================================================       
# # # method overriding...                              # 

# print(isinstance((1,2,4),tuple))      

# class Parent:
#     def __init__(self):                                          #2
#         self.value = 5                                           #3
#     def get_value(self):        
#         return self.value                              

# class Child(Parent):                      
#   # pass 
#     def get_value(self):
#         return self.value + 1  
     
# class Child2(Parent):                                      
#     def get_value(self):                                                 #5
#         return self.value + 2     
    
# c = Child2()                                                             #1     
# # print(c.get_value())                                                  #2   

# # print(isinstance(c,Parent))           
# # print(isinstance(c,Child))           

# print(issubclass(Child,Parent))         
         

################################################################################                              

# # # # # # dunder 

# class Phone:
#     def __init__(self,brand, model, price):                
#         self.brand=brand
#         self.model=model
#         self.price=price 

#     def phone_name(self):
#         return f"{self.brand} {self.model}"

#     def __str__(self):                                           #        
#         return f" {self.brand} {self.model} and {self.price}"      

#     def __repr__(self):
#         return f" Phone(\'{self.brand}\' ,{self.model}, {self.price})"                                 # f"\'"  =  '
    
# my_phone=Phone("noika", "1100", 1000)  
# print(my_phone)         ###     guy friends         friend
# print(str(my_phone))    ###     guy                 kabir singh                                        
# print(repr(my_phone))   ###    she is pretty        preeti 


# # # ==========================================================================
# dunder 

# class Phone:
#     def __init__(self,brand, model, price):                                         #2
#         self.brand=brand
#         self.model=model
#         self.price=price

#     def phone_name(self):                                                           #6
#         return f"{self.brand}{self.model}{self.price}"            # "ankit1000222"  >>>> 12

#     def __str__(self):
#         return f" {self.brand} {self.model} and {self.price}"

#     def __repr__(self):
#         return f" Phone(\'{self.brand}\' ,\'{self.model}\', {self.price})"

#     def __len__(self):                              #4
#         return len(self.phone_name())               # len("ankit1000222")
                                       
# my_phone=Phone("ankit",1000,222)                                 #1
# # print(str(my_phone))
# # print(my_phone.__str__())   
# print(len(my_phone))                                           #3
# print(my_phone.__len__())                                             #3



# # # # =====================================================================


# class Phone:
#     def __init__(self,brand, model, price):
#         self.brand=brand
#         self.model=model
#         self.price=price    
#     def phone_name(self):
#         return f"{self.brand} {self.model}"
#     def __str__(self):
#         return f" {self.brand} {self.model} and {self.price}"
#     def __repr__(self):
#         return f" Phone(\'{self.brand}\' ,\'{self.model}\', {self.price})"
#     def __len__(self):
#         return len(self.phone_name())

#     def __add__(self, other):  
#         return self.price + other.price              

# my_phone=Phone("noika","11000",1000)   
# my_phone2=Phone("noika","11000",1200)    

# print(my_phone + my_phone2)             


# # # # ==============================================================
# # method overloading not supported in python.........                    

# class A():
#   def a(x,y):             
#     print(x+y) 

# class B(A):
#   def a(x,y,z):                     
#     print(x+y+z)   

# a=B()  
# print(a(5,4,7)) 

# # # =====================================


# def product(a, b): 
# 	print("a") 

# def product(a, b, c): 
# 	print("b") 


# product(4, 5)  
# # product(20,2,6)

# # #  


# # # =============================================================================



# # # len()          

# # # string ,     list     ,   tuple  ,,   set   ,,,  dict                                        

# # # len()               # sting  , list , set , tuple , dict ,............. 

# # # ===============================================================

# # #polymoriphism      
# poly >> many  ||| morphism >>> forms 

# len() 


# # #  means that we can apply same method in different data types it is poly morphism,,, 

# # # ex,,, we can apply len()  in many datatypes

# # # len()           ..........    +    =====    "ankit"   list  ,, 



# # ===============================================================
# # # =====================================================================================================================


# # # finished ======================================================
# # # ===============================================================
# # # ===============================================================
# # # ===============================================================
# # # ===============================================================

# def fun(a,b):
#     return a+b

# def fun(a,b,c):
#     return a+b+c 



# print(fun(4,6))  

##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################


































