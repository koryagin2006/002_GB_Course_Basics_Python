# dict - неупоряодченные коллекции произвольных объектов с доступом по ключу
friends = ['Max', 'Leo', 'Kate']
print(friends)  # <class 'list'>
friend = friends[0]
print(friend)  # <class 'str'>

friend = {'name': 'Max', 'age': 23}  # <class 'dict'>

print(friend['age'])  # сколько лет другу
friend['has_car'] = True  # добавление пары в словарь
print(friend)  # {'name': 'Max', 'age': 23, 'has_car': True}
friend['has_car'] = False  # замена пары в словаре
print(friend)  # {'name': 'Max', 'age': 23, 'has_car': False}
del friend['age']  # удаление пары
print(friend)

if 'age' in friend:
    print('Есть возраст')
else:
    print('Возраста нет')
print('-------------')

friend = {
    'name': 'Max',
    'age': 23,
    'has_car': True
}

# по ключам
for key in friend.keys():
    print(key)
    print(friend[key])
    print('-----')

for key in friend:
    print(key)
    print(friend[key])
    print('-----')

# по значениям
for value in friend.values():
    print(value)

# по парам
for item in friend.items():
    print(item)

for key, value in friend.items():
    print(key)
    print(value)
    print('----')