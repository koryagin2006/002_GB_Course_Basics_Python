age = int(input('Введите свой возраст: '))

# Если возраст меньше 18 => Доступ запрещен
if age < 18:
    print('Доступ запрещен')
elif age == 18:
    print('Вам ровно 18 лет')
else:
    print('Доступ разрешен')
    # проверим на юбилей
    if age % 5 == 0:
        print('У вас юбилей в этом году')

print('Какие-то действия')
print('end')
print('------------------>')

number = 43
value = int(input('Введите число от 1 до 100'))

if value == number:
    print('Вы угадали')
else:
    if value > number:
        print('Нужно меньше')
    else:
        print('Нужно больше')
