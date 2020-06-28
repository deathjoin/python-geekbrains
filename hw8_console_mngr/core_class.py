import os
import datetime
import shutil


class Core:
    script_dir = ''

    @staticmethod
    def create_file(name, text=None):
        with open(name, 'w', encoding='utf-8') as f:
            if text:
                f.write(text)

    @staticmethod
    def create_folder(name):
        try:
            os.mkdir(name)
        except FileExistsError:
            print('Такая папка уже есть')

    @staticmethod
    def get_list(folders_only=False):
        result = os.listdir()
        if folders_only:
            result = [f for f in result if os.path.isdir(f)]

        return result

    @staticmethod
    def delete_file(name):
        if os.path.isdir(name):
            os.rmdir(name)
        else:
            os.remove(name)

    @staticmethod
    def copy_file(name, new_name):
        if os.path.isdir(name):
            try:
                shutil.copytree(name, new_name)
            except FileExistsError:
                print('Такая папка уже есть')
        else:
            shutil.copy(name, new_name)

    @staticmethod
    def save_info(message):
        current_time = datetime.datetime.now()
        result = f'{current_time} - {message}\n'

        # логи всегда пишутся в директорию, где стартанул скрипт
        with open(f'{Core.script_dir}/log.txt', 'a', encoding='utf-8') as f:
            f.write(result)

    # Метод смены директории, записываёт её в файл, потому что надо сохранять между запуском программы
    @staticmethod
    def change_dir(dir):
        if os.path.isdir(dir):
            # файл настроек с текущим путём всегда в директории, где стартанул скрипт
            with open(f'{Core.script_dir}/cwd.txt', 'w', encoding='utf-8') as f:
                os.chdir(dir)
                f.write(os.getcwd())
        else:
            print('Это не папка или её нет')

    # Метод получения рабочей директории, в которую мы когда-то переместились
    @staticmethod
    def get_dir():
        try:
            with open(f'{Core.script_dir}/cwd.txt', 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return os.getcwd()

    # Метод установки директории скрипта
    @staticmethod
    def script_dir(dir):
        if dir:
            Core.script_dir = dir
