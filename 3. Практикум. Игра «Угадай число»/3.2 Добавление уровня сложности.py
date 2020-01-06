# Шаг 1. Загадать число
import random

number = random.randint(1, 100)
# print(number)
user_number = None
while number != user_number:
    user_number = int(input('Введите число: '))
    if number < user_number:
        print('Ваше число больше загаданного')
    else:
        print('Ваше число меньше загаданного')
print('Победа!')
