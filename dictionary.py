phone_numbers = {}
n = int(input('Enter n:'))
for _ in range(n):
    data = input('Enter number and name:').split()
    number, name = data[0], data[1]
    # наполняем словарь ключами и значениями
    if name in phone_numbers:
        phone_numbers[name] += ' ' + number
    else:
        phone_numbers.setdefault(name, number)

# Обработка запросов пользователя
m = int(input('Enter m:'))
for _ in range(m):
    name_query = input('Enter your query:')
    answer = phone_numbers.get(name_query, 'Неизвестный номер')
    print(answer)
