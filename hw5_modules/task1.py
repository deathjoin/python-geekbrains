# Модули и библиотеки. Задание1
# Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
# Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.

import os
path = os.getcwd()


def dir_creator():
    for i in range(1, 10):
        os.mkdir(f'{path}/dir_{i}')


def dir_destroyer():
    for i in range(1, 10):
        os.rmdir(f'{path}/dir_{i}')