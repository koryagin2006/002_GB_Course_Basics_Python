# Модуль os
# Функции для работы с операционной системой
# Не зависит от конкретной ОС

# Функции и переменные os
#  - name - имя операционной системы
#  - chdir - смена текущей директории
#  - getcwd() - текущая рабочая директория
#  - mkdir() - создание директории (папки)
#  - os.path - модуль для работы с путями
#  - и многие другие

import os

# Имя OS
print(os.name)  # nt

# текущая рабочая директория
print(os.getcwd())  # C:\.......\GB_Course_Basics_Python\5. Модули и библиотеки

# создаем новый путь
# new_path = os.path.join(os.getcwd(), 'new_f')

# создаем папку по новому пути
# os.mkdir(new_path)
print('---')
# Модуль sys
#  - Взаимодействие с интерпретатором Python
# Функции и переменные sys
#  - executable - путь к интерпретатору Python
#  - exit() - выход из Python
#  - platform - информация об ОС
#  - path - список путей поиска модулей
#  - argv - список аргументов командной строки
#  - и многие другие

import sys

# путь до интерпретатора
print(sys.executable)  # C:\Users\carne\Desktop\GeekBrains...\GB_Course_Basics_Python\venv\Scripts\python.exe

# Информация о платформе
print(sys.platform)  # win32

# Выход из python
# sys.exit()
# print('Этот код мы уже не выполним')  # не выполняется

# sys.path
#  - очень важная переменная
#  - она хранит пути? по которым Python ищет модули
#  - она имеет изменяемый тип данных list
#  - таким образом мы можем изменять эту переменную

# мы можем импортировать модуль math
import math
# но не можем импортировать наш модуль на диске C:
# import my_module

# как питон находит модули?
import sys

print(type(sys.path))  # <class 'list'>
for p in sys.path:
    print(p)  # выводит список путей модулей