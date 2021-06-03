import json

with open('manager_sales.json', 'r') as file:
    data = json.load(file)

for str in data:
    proceeds = []
    for car in str['cars']:
        proceeds.append(car['price'])
    print(str['manager']['first_name'], str['manager']['last_name'], sum(proceeds))