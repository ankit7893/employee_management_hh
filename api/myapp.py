import requests

URL =  'http://127.0.0.1:8000/stuinfo/4'

r= requests.get(url=URL)  

# print(r)
# print(type(r))
data = r.json() 

# print(r.json()) 
# print(type(r.json())) 

# print(type(data)) 
print(data)



