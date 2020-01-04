friend = 'максим'
print(friend)  # <class 'str'>
print('say "Hello"')
print('Первая бука имени друга', friend[0])
print('Предпоследняя бука имени друга', friend[-2])

# срезы
print(friend[1:4])  # - c второго по третий символ
print(friend[:4])  # - c начала строки по третий символ
print(friend[3:])  # - c четветрого по конец строки

# функция len
print(len(friend))  # длина строки, сколько в ней символов
print(friend.find('а'))  # ищем символ а в строке
friends = 'Максим Леонид'
print(friends.split())  # разделение через пробел
print(friend.upper())  # приведение к верхнему регистру
print(friend.lower())  # приведенние к нижнему регистру
print(friend.isdigit())  # строка состоит из чисел

print(friend[0].upper() + friend[1:])

# форматирование строк
name = 'Leo'
age = 30
# 1. Конкатенация (не рекомендуется)
hello_str = 'Привет, ' + name + ', тебе ' + str(age) + ' лет'
print(hello_str)
# 2. %
hello_str = 'Привет, %s, тебе %d лет' % (name, age)
print(hello_str)
# 3. format
hello_str = 'Привет, {}, тебе {} лет'.format(name, age)
print(hello_str)


# пример
top5 = 'Первые 5 мест на соревнованиях: 1. иванов 2. петров 3. сидоров 4. орлов 5. соколов'
    # Поздравляем 1 ИВАНОВ 2. ПЕТРОВ 3. СИДОРОВ с успехом!
start = top5.find('1')
end = top5.find('4')
top3 = top5[start:end]
result = 'Поздравляем {} с успехом'.format(top3.upper())
print(result)