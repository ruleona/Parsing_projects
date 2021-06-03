string = input()
d = {}

for char in string:
    d[char] = string.count(char)

#находим максимальное количество вхождений символа в строку
max_value = 0
for value in d.values():
    if value > max_value:
        max_value = value

#создаю список с ключами, у которых максимальное знчение value
chars = []
for key, value in d.items():
    if value == max_value:
        chars.append(key)

if len(chars) == 1:
    print(chars[0])
else:
    #перебираю строку в обратном порядке до первого вхождения
    for char in string[::-1]:
        if char in chars:
            print(char)
            break