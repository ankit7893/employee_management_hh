# bubble sort  


# l= [4,3,2,1]         ## length = 4            ## iteration = length -1    ######  first bubble -- length -1 

# 4,3,2,1                ## iteration = 1           bubble = 3   
# 3,4,2,1
# 3,2,4,1
# 3,2,1,4 


# 2,3,1,4                    ## iteration = 2           bublle =2 
# 2,1,3,4

# 1,2,3,4                        ### iteration = 3         bubble =1 


# # l=[2,324,24,2342,12323,44454,67765,46876,3442,13,2311,244]
# l= [4,3,2,1]   
# # 3,4,2,1
# # 3,2,4,1
# # 3,2,1,4 

# # 2,3,1,4 
# # 2,1,3,4

# # 1,2,3,4 
# for i in range(len(l)-1, 0, -1):      ## i= 1 
#     for j in range(i):                 ###  j = 0       
#         if l[j] > l[j+1]:       ##  2>1    
#             l[j],l[j+1] = l[j+1] , l[j]       ###  

#         print(l)
#     print()

# print(l)
#
#######################################################################################
#######################################################################################
#######################################################################################
#######################################################################################

# sequencial search 


# l= [2, 13, 24, 34,47,53,68,73,89,94,103,115,129,137,145,153,167] 
# s =  153  



# count = 0 
# for i in range(len(l)):
#     count=count+1
#     if l[i]==s:   ## 2==153 
#         print(i)  
#         break


# print(count)



####################################################################################
# binary search (applicable on only sorted list)


# l= [2, 13, 24, 34,47,53,68,73,89,94,103,115,129,137,145,153,167] 
# # 
# s =  153  

# 153==73  false >>>   
# 153==129  false >> 
# 153== 145  False >>> 


# list= [2, 13, 24, 34,47,53,68,73,89,94,103,115,129,137,145,153,167,199]
# #                                                   m   l            h 

# l=0         ###  l=0
# h=len(list)-1  ## h=17
# s =  153       ## s=153
# found = False  ## 

# while l<=h:            ###  
    
#     m = (l+h)//2   ## m =  (14+17)//2  =  15 
#     if s==list[m]:            ##  153 == 153       True
#         print(f"found at index {m} ")
#         found=True
#         break
#     elif s>list[m]:             ### 153>137  True  
#         l=m+1                 ## l=  13+1 = 14 
#     else:
#         h=m-1 
# else:
#     print("not found")


####################################################################################


# pattern >

# *                ### row=1  ,, i= 0  ,   j=1  
# * *              ## row=2   ,, i=1    , j=2 
# * * *           ## row =3     ,, i=2 , j=3 
# * * * * 
# * * * * * 


# n=int(input("how many rows you want: "))
# for i in range(n):               #### 
#     for j in range(i+1):
#         print("*",end=" ")

#     print()

        
        
#####################################################################################




# s= "an234ki24df234fe2342c245t"

# sum=0 
# for char in s:
#     if char.isdigit():
#         sum = sum + int(char)

# print(sum)



# print(ord("&"))           



# print("ankit",sep=" ", end=" ")









# 



































