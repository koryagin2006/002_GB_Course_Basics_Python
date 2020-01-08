# Шаг 1. Загадать число
import random

number = random.randint(1, 100)
# print(number)
user_number = None
count = 0  # введем количество попыток
levels = {1: 10, 2: 5, 3: 3}  # уровни сложности
level = int(input('Выберите уроверь сложности 1-3: '))
max_count = levels[level]  # максимально количество попыток

while number != user_number:
    count += 1
    if count > max_count:
        print('Вы проиграли')
        break
    print(f'Попытка № {count}')
    user_number = int(input('Введите число: '))
    if number < user_number:
        print('Ваше число больше загаданного')
    else:
        print('Ваше число меньше загаданного')
else:
    print('Победа!')