import requests
import json 


URL  = 'http://127.0.0.1:8000/studentapi/'

def get_data(id= None): ### 
    data = {}                ### complete data  
    if id is not None: 
        data = {'id':id}     ##   1 record        
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)  ### 
    print(r) 
    data= r.json()  
    print(data)

# get_data(3) 


def post_data():
    data = {
        'name':'arnav',
        'roll':5,
        'city':"delhi"
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL, data = json_data)
    data = r.json()
    print(data) 

# post_data()




def update_data():
    data = {
        'id':1,
        'name':'sree',
        'roll':101,
        'city': "london"
    }

    json_data = json.dumps(data)
    r = requests.put(url=URL, data = json_data)
    
    
    data = r.json()
    print(data)

# update_data()
#



def update_data():
    data = {
        'id':1,
        'name':'kalpna',
    }

    json_data = json.dumps(data)
    r = requests.patch(url=URL, data = json_data)
    
    data = r.json()
    print(data)

# update_data()
#



def delete_data():
    data = {'id':1}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data = json_data)
    data = r.json()
    print(data)

delete_data()

