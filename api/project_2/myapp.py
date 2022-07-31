
import requests
import json

URL = 'http://127.0.0.1:8000/stucreate/'

data  = {
    'name': 'sapna',
    'roll':100,
    'city': 'mumbai'
}

json_data  =  json.dumps(data)

r= requests.post(url=URL, data = json_data)  
print(r)
data = r.json()
print(data)








