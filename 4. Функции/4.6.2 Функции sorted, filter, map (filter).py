# filter
# фильтрация последовательности
# filter(function, iterable)
# аргументы: функция фильтрации, последовательность

# набор чисел
numbers = (1, 2, 3, 4, 5, 6, 7, 8)


# получить только четные числа
def is_even(number):
    return number % 2 == 0


result = filter(is_even, numbers)
print(result)
print(list(result))
print('----')
# набор строк
names = ['Max', 'Leo', 'Kate']

# получить строки больше 3 символов
# print(filter(names, ))
print(list(filter(lambda name: len(name)>3, names)))  # ['Kate']