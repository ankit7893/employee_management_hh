#
# class Mobile:
#     def __init__(self):
#         self.model = 'redmi 10'
    
#     def get_model(self):        ###  getter method ||| accessor method  
#         return self.model

#     def set_model(self):          ## setter  ||| mutator 
#         self.model = 'iphone 11'

# obj = Mobile()
# print(obj.get_model()) 
# print(obj.set_model())   
# print(obj.get_model())

######################################################################
# govt AK 47  
# army || air force ||| navy 


# gun  = 
# Area =  
##################################################################
# abstract classes 

# from abc import ABC  , abstractmethod 

# class Father(ABC):
#     @abstractmethod
#     def disp(self):
#         pass 

#     def show(self):
#         print("concrete method")


# class Child(Father):
#     def disp(self):
#         print("child class") 
        
# c= Child()
# c.disp()
# c.show()
############################################################
# from abc import ABC  , abstractmethod
# from traceback import print_tb 

# class DefenceForce(ABC):
#     @abstractmethod
#     def area(self):
#         pass           ### land || sky || sea 
    
    
#     def gun(self):
#         print("Gun >>>  AK 47")


# class Army(DefenceForce):
#     def area(self):
#         print("area>>>>  land ")
    

# class Airforce(DefenceForce):
#     def area(self):
#         print("area >>>>  sky  ")
    
#     def gun(self):
#         print("Akkk  34")

# class Navy(DefenceForce):
#     def area(self):
#         print("area >>>>   sea ")


# af = Airforce()
# # af = Navy()
# af.area()
# af.gun()

####################################################################

# l= >>>> 100   >>>> 0.22  milliseconds 
# l  >>>> 1000  >>>>  2.00  milliseconds  


# t =  a*n             + b  
# n=100    ## b=10 
#  t= 1*100            +  10 
# n= 10000 
# t= 1*10000           +  10 
# n= 1000000000000000 
# t= 1*100000000000000 + 10 

# t= a*n 
# rule 
# 1. keep fastest growing term 
# 2. drop constant 

# t= O(n) 

###########################################################

# def fun(n):
#     l= []             ## b 
#     for i in n:           ##### 
#         l.append(i*i)             
#     return l          ## b 

# n=[2,3,4,1,1]       
# print(fun(n)) 

# # a*n       
# # O(n) 



# def fun(a,b):
#     c = a+b 
#     return c  

# O(1)

#################################
# l=[2,3,4,14]        ##
# c=0 
# for i in range(len(l)):
#     for j in range(len(l)):
#         c=c+1
#         if l[i]==66:
#             break
#         print("vatsal ")   
# print("code finished")
# print(c)

# # t= a*n**2  +  b  
# t= 16   ()


# for i in range(4):         ##  
#     if i==10:
#         break
#     for j in range(4):       ## 4*4 = 16 
#         print("vatsal")


# O(n2)

################################################################


# l=[132,2,4,2,3,23,]
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i]==l[j]:
#             break 


# for i in range(len(l)):
#     if i==8:
#         break 

# t= a*n2  +  b*n  + c  
# t= a*n2  
# O(n2)










# t= a*n**2             ## 25          5
# n=1000                5 

# t= O(n2) 

# rule 
# 1. keep fastest growing term 
# 2. drop constant 
##################################################################
# time complexity 
# space complexity 

# l = [4,9,15,34,45,57,65,87,93]

# for i in range(len(l)):         ## 9  
#     if l[i]==93:
#         print(i)

# O(n)                #######



# l = [4,9,15,34,45,57,65,87,93]

# s=87
# iteration =1    >>>  n/2  
# iteration = 2  >>>  (n/2)/2   = n/4   = n / 2**2
# iteration  =  3   >>> (n/4)/2  =  n/8   = n / 2**3


# k= n  /  2**k 
#  k=1
# 1= n/2**k 
# n= 2**k 
##############################################







