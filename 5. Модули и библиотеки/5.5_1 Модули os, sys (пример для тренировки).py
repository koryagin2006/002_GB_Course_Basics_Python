# Пример для тренировки:
#   В папке с модулем создать 5 подпапок, названия которых состоят из платформы,
#   на которой запущен интерпретатор и порядкового номера, начиная с 1: win32_1, win_32_2, … Платформа может быть другой.

import sys, os

name = sys.platform

# for i in range(1, 6):
#     new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
#     os.mkdir(new_path)

os.makedirs('{}\\{}'.format(os.getcwd(),'5.5_1 Пример'),exist_ok=True)

for i in range(1, 6):
    new_path = os.path.join('{}\\{}'.format(os.getcwd(), '5.5_1 Пример'), '{}_{}'.format(name, i))
    os.makedirs(new_path,exist_ok=True)
