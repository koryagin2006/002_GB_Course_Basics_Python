# Функция - тоже объект
# Её можно записать в переменную.
def some_f():
    return 10


result = some_f()
print(result)  # 10

a = some_f
print(a)  # <function some_f at 0x0065F6E8>
print(type(a))  # <class 'function'>
print(a())  # 10

print('----')


# Её можно передавать параметром в другие функции.
def f():
    print('hello from other f')


def to(f_param):
    # параметром будет функция, поэтому в тебе функции to мы ее вызовем
    f_param()


# проверим
to(f)  # hello from other f
print('----')

# Применение:
# возможность не только входных данных, но и входных функций
# внутри функции переменными являются
# алгоритмпоследовательность действий
# сами действия
numbers = [1, 2, 3, 4, 5, 6, 7, 8]


# def my_filter(numbers):
#     result = []
#     for number in numbers:
#         if number % 2 == 0:
#             result.append(number)
#     return result

def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result


# для поиска четных чисел
def is_even(number):
    return number % 2 == 0


print(my_filter(numbers=numbers, function=is_even))  # [2, 4, 6, 8]


# если нужны нечетные числа
def is_not_even(number):
    return number % 2 != 0


print(my_filter(numbers=numbers, function=is_not_even))  # [1, 3, 5, 7]


# если нужны чсла больше 4
def big_4(number):
    return number > 4


print(my_filter(numbers=numbers, function=big_4))  # [5, 6, 7, 8]