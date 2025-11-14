import os.path
import shutil
from shutil import ReadError


def untar_folder(command_line: list, current_dir: str) -> str:
    """
     Функция разархивирует файлы с расширением tar
    :param command_line: список, где находятся файлы для разархивации
    :param current_dir: строка, где указан путь текущей директории
    :return: Возвращает результат выполнения функции: успех или ошибка
    """
    if command_line:
        try:
            for file in command_line:
                print(os.path.join(current_dir, file),current_dir )
                shutil.unpack_archive(filename=str(os.path.join(current_dir, file)), extract_dir=current_dir, format='tar')
                print('1')
        except FileNotFoundError:
            print('Каталог не найден')
            return 'Каталог не найден'
        except IsADirectoryError:
            print('Передан каталог, не файл')
            return 'Передан каталог, не файл'
        except ReadError:
            print('Передан не tar файл')
            return 'Передан не tar файл'
        return 'Success'
    else:
        print('Недостаточно аргументов для команды')
        return 'Недостаточно аргументов для команды'
