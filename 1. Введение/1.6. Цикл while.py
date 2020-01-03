# цикл while
# задвать вопросы, пока пользователь не введет правильный ответ

name = input('Кто создатель python? ')
while name != 'Гвидо':
    print("Неверно")
    name = input('Кто создатель python? ')
print('Верно')

# вывод чисел от 0 до 100
number = 0
while number <= 100:
    print(number)
    # number = number +1
    number += 1

# вывод чисел от 0 до n
number = 0
n = int(input('Введите n: '))
while number <= n:
    print(number)
    # number = number +1
    number += 1

# вывод четных чисел от 0 до n
number = 0
n = int(input('Введите n: '))
while number <= n:
    if number % 2 == 0
        print(number)
    # number = number +1
    number += 1
