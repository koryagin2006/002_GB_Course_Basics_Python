# # sorted
# сортировка последовательности
# sorted(iterable, *, key=None, reverse=False)
# аргументы: последовательность, ключ для сортировки, порядок

numbers = [1, 5, 3, 5, 9, 7, 11]
# сортировка по возрастанию
print(sorted(numbers))  # [1, 3, 5, 5, 7, 9, 11]
# сортировка по убыванию
print(sorted(numbers, reverse=True))  # [11, 9, 7, 5, 5, 3, 1]

names = ['Max', 'Alex', 'Kate']
# сортировка по алфавиту
print(sorted(names))  # ['Alex', 'Kate', 'Max']

cities = [('Москва', 1000), ('Лас-Вегас', 500), ('Антвервпен', 2000)]
# сортировка по имени
print(sorted(cities))  # [('Антвервпен', 2000), ('Лас-Вегас', 500), ('Москва', 1000)]


# сортировка по численности
# def by_count(city):
#     return city[1]
# print(sorted(cities, key=by_count))  # [('Лас-Вегас', 500), ('Москва', 1000), ('Антвервпен', 2000)]
print(sorted(cities, key=lambda city: city[1]))  # [('Лас-Вегас', 500), ('Москва', 1000), ('Антвервпен', 2000)]