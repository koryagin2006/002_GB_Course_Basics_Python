# Функции - элемент кода (подпрограмма), к которому можно обратитьсяиз другого места программы
# Полезные встроенные:
# abs - модуль числа
print(abs(+7))
# min, max - минимальное, максимальное значение
numbers = [5, 15, 7, 1, -9, 0]
print(min(numbers))
print(max(numbers))
# round - округление числа
print(round(10.9872, 2))
# sum - сумма элементов последовательности
print(sum(numbers))
# enumerate - нумерация последовательности
winners = ['Leo', 'Max', 'Kate']
for number, winner in enumerate(winners, 1):
    print(number, winner)
print('----')
# Пример
# Пользователь вводит 3 числа. Найти минимальное из них, максимальное из них, их сумму и вывести результат на экран.
numbers = []
for i in range(3):
    number = int(input('Введите число: '))
    numbers.append(number)
print('max number =', max(numbers))
print('min number =', min(numbers))
print('sum numbers =', sum(numbers))