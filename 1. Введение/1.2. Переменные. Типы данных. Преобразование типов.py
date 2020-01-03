# верно и типы данных
person_name = 'Max'  # <class 'str'>
age = 30  # <class 'int'>
period = 3.2  # <class 'float'>
is_good = True  # <class 'bool'>
person = None  # <class 'NoneType'>
# неверно
pn = 'Max'
a = 30
p = 3.2
q = True
pp = None

# Приведение типов
birthday_year = '1988'
print(type(birthday_year))

period = 20
print(type(period))

# age = birthday_year + period # -> TypeError: can only concatenate str (not "int") to str
age = int(birthday_year) + period  # математическое сложение
print(age)

some_str = birthday_year + str(period)  # конкатенация
print(some_str)
