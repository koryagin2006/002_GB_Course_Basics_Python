# Множества set - неупорядоченные коллекции, содержащие неповторяющиеся элементы
# Во множестве не может быть 2-х одинаковых элементов

cities = ['Las Vegas', 'Paris', 'Moscow', 'Paris', 'Moscow']
print(cities)  # <class 'list'>
cities = set(cities)
print(cities)  # <class 'set'>
# действия с множествами
cities.add('Burma')  # добавление уникального элемента
print(cities)

cities.remove('Moscow')  # удаление элемента
print(cities)

print(len(cities))  # подсчет количества элементов множества
print('Paris' in cities)  # True

for city in cities:
    print(city)
print('----')

# операции со множествами
# семейная пара собирается в отпуск
# вещи супругов:
max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}
kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}

# какие вещи взяли супруги вместе
print(max_things | kate_things)
# какие вещи повторяются
print(max_things & kate_things)
# какие вещи взял max, но не взяла kate
print(kate_things - max_things)
# какие вещи взяла kate, но не взял max
print(max_things - kate_things)