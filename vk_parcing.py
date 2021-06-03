import json

with open('group_people.json') as file:
    data = json.load(file)

# print(*data, sep='\n')
max_count = 0
id_group = ''
for group in data:
    count = 0
    for human in group['people']:
        if human['gender'] == 'Female' and human['year'] > 1977:
            count += 1
    if count > max_count:
        max_count = count
        id_group = group['id_group']
    print(group['id_group'], count, max_count)
print(id_group, max_count)
