# Импорт из своих модулей
#  - Совершается так же, как и из стандартных модулей
#  - При импорте нужно учитывать путь до модуля
# import first_module
# import folder.second_module

import mod_a

print(mod_a.foo)  # foo A
mod_a.bar()  # bar A

from folder_b.mod_b import foo, bar

print(foo)  # foo B
bar()  # bar B
print('----')

# Модули со скриптами
#  - При любом варианте импорта скрипты будут выполняться
#  - Если не указано никаких условий (if __name__ == ‘__main__’)
#  - Это обязательно нужно учитывать при импорте

