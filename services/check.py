import requests
import time
import random 
print('Вы хотите использовать тестирование для 0 - uvicorn, 1 - docker_compose')

url = ''
while url == '':
    option = int(input())
    if option == 0:
        url = 'http://127.0.0.1:8000/api/prices'
    elif option == 1:
        url = 'http://127.0.0.1:1702/api/prices'
    else:
        print('Введите 1 или 0')

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}



for i in range(50):

    data = {
        "build_year": random.randint(1990,2024),
        "building_type_int": random.randint(1,5), 
        "latitude": random.uniform(55.5, 56.0), 
        "longitude": random.uniform(37.5, 38.0),
        "ceiling_height": random.uniform(2.0,3.0), 
        "flats_count": random.randint(20,200), 
        "floors_total": random.randint(5,30), 
        "has_elevator": random.choice([True, False]), 
        "floor": random.randint(5,29),
        "kitchen_area": random.uniform(9.0,11.0), 
        "living_area": random.uniform(10.000000,50.000000),
        "rooms": random.randint(1,5),
        "is_apartment": random.choice([True, False]), 
        "total_area": random.uniform(20.000000,90.000000)
    }
    
    user_id = {'user_id': i}
    response = requests.post(url, headers=headers, json=data, params=user_id)
    
    if i == 30:
        time.sleep(30)
    

    time.sleep(2) 