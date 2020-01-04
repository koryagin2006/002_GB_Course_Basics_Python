# Тип данных list

empty_list = []  # можно объявить пустой список
friends = ['Max', 'Leo', 'Kate']  # можно сразу заполнить список элементарми
print(type(friends))  # <class 'list'>
print('Второй друг', friends[1])  # Доступны индексы
print('Первый друг с конца', friends[-1])  # Доступны индексы
print(len(friends))  # количество элементов, в данном случае - друзей

friends.append('Ron')  # добавляет элемент
print(friends, len(friends))

print(friends.pop())  # удаляет последний элемент + выводит его на экран
print(friends)

friends.clear()
print(friends)
friends = ['Max', 'Leo', 'Kate']

friends.remove('Kate')
print(friends)
del friends[0]
print(friends)

# Другие методы списка list
