# lambda-функции
# применяются для создания анонимных функций по месту их использования
# Синтаксис:
# lambda <входные параметры> : <результат>
numbers = [1, 2, 3, 4, 5, 6, 7, 8]


def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result


# def is_even(number):
#     return number % 2 == 0

# для поиска четных чисел

print(my_filter(numbers=numbers, function=lambda number: number % 2 == 0))  # [2, 4, 6, 8]

# если нужны нечетные числа
print(my_filter(numbers=numbers, function=lambda number: number % 2 != 0))  # [1, 3, 5, 7]

# если нужны чсла больше 4
print(my_filter(numbers=numbers, function=lambda number: number > 4))  # [5, 6, 7, 8]
