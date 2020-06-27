# Модули и библиотеки. Задание3
# Создайте модуль main.py.
# Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций.
# Вызовите каждую функцию в main.py и проверьте что все работает как надо.

# Все Задания разделены по подпапкам, поэтому .task
from hw5_modules.task1 import *
from hw5_modules.task2 import get_random


dir_creator()
dir_destroyer()
print(get_random(['Apple', 'Orange', 'Brains', 'Geek']))
