import sys
import os
from core_class import Core

# Устанавливаем директорию скрипта, логи и файлы конфигурации будут здесь
Core.script_dir(os.getcwd())

Core.save_info('Старт')

# Переводим текущую рабочую директорию на ту, в которую мы переместились ранее или на директорию вызова скрипта
os.chdir(Core.get_dir())
try:
    command = sys.argv[1]
except IndexError:
    print('Не указана команда')
else:
    if command == 'cd':
        try:
            name = sys.argv[2]
            Core.change_dir(name)
        except IndexError:
            print('Не указано имя папки')
    elif command == 'list':
        print(Core.get_list())
    elif command == 'create_file':
        try:
            name = sys.argv[2]
            Core.create_file(name)
        except IndexError:
            print('Не указано имя файла')

    elif command == 'create_folder':
        try:
            name = sys.argv[2]
            Core.create_folder(name)
        except IndexError:
            print('Не указано имя папки')
    elif command == 'delete':
        try:
            name = sys.argv[2]
            Core.delete_file(name)
        except IndexError:
            print('Не указано, что удалять')
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
            Core.copy_file(name, new_name)
        except IndexError:
            print('Не указано имя или имена')
    elif command == 'help':
        print('list - списко файлов и папок')
        print('create_file - создание файлов')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')

Core.save_info('Конец')
