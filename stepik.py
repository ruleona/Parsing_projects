# MIN_DRIVING_AGE = 18
#
# def allowed_driving(name, age):
#     global MIN_DRIVING_AGE
#     if age >= MIN_DRIVING_AGE:
#         print(f'{name} еще рано садиться за руль')
#     else:
#         print(f'{name} может водить')
#
# allowed_driving('bob', 23)
# allowed_driving('steven', 5)

def format_namelist(lst):
    if len(lst) == 0:
        return ''
    values = []
    answer = ''
    for v in lst:
        values.append(v['name'])
    if len(lst) == 1:
        answer = values[0]
    elif len(lst) == 2:
        answer = values[0] + ' и ' + values[1]
    else:
        answer = ', '.join(values[:-1]) + ' и ' + values[-1]
    return answer

print(format_namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))