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

# Оператор in
hero = 'Superman'
if hero.find('man') != -1:  # проверяем, есть ли в слове Superman слово man
    print('Есть')

if 'man' in hero:
    print('Есть')

goals = ['стать гуру python', 'здоровье', 'накормить кота']
if 'здоровье' in goals:
    print('Все хорошо')

# Тип кортеж - список, который нельзя менять
# Пользователь вводит количеств оучастников соревнований
# Пользователь вводит участниов и их места
# 1. Вывод участников по-алфавиту
# 2. Поздравить 3-х победителей

print('Соревнования по python')
count = int(input('Введите количество участников: '))
i = 1
members = []
while i <= count:
    name = input('Кто занял {} место '.format(i))
    members.append(name)
    i += 1

print('В соревнованиях учавствовали: ', sorted(members))
result = members[:3]
result = 'Победители: {}. Поздравляем!'.format(result)
print(result)