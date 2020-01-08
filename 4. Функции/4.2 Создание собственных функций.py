# Функция. Простой разделитель.
# Простой разделитель - нет параметров, нет возврата.

def print_sep():
    print('-' * 100)


print('Моя первая функция')
# print_sep()  # отрабатывает код внутри функции  print('-' * 100)
# print('Красивый разделитель')
# print('Что если их будет много')
# print_sep()
print_sep()  # отрабатывает код внутри функции  print('-' * 100)


# Параметры и результат
# Меняем знак разделителя - 1 параметр, нет возврата.
def print_sep_2(sep):  # 1 параметр - тип разделителя
    print(sep * 100)


print_sep_2('*')
print_sep_2('-')


# Меняем знак и длину - 2 параметра, нет возврата.
def print_sep_3(sep, sep_len):  # 2 параметра - тип разделителя и его длина
    print(sep * sep_len)


print_sep_3('-', 50)


# Используем разделитель в тексте
def get_sep(sep, sep_len):  # 2 параметра - тип разделителя и его длина
    return sep * sep_len


print(get_sep('*', 30))

sep = get_sep('-', 50)
text = 'Hello {} Func {}'.format(sep, sep)
print(text)
