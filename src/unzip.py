import os.path
import shutil
from shutil import ReadError


def unzip_folder(command_line: list, current_dir: str) -> str:
    """
    Функция разархивирует файлы с расширением zip
    :param command_line: список файлов для разархивирования
    :param current_dir: строка, где указан путь до текущей директории
    :return: Возвращает результат выполнения функции: успех или ошибка
    """
    if command_line:
        try:
            for file in command_line:
                print(os.path.join(current_dir, file),current_dir )
                shutil.unpack_archive(filename=str(os.path.join(current_dir, file)), extract_dir=current_dir, format='zip')
                print('1')
        except FileNotFoundError:
            print('Каталог не найден')
            return 'Каталог не найден'
        except IsADirectoryError:
            print('Передан каталог, не файл')
            return 'Передан каталог, не файл'
        except ReadError:
            print('Передан не zip файл')
            return 'Передан не zip файл'
        return 'Success'
    else:
        print('Недостаточно аргументов для команды')
        return 'Недостаточно аргументов для команды'
