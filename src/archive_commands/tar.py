import os.path
import shutil


def tar_folder(command_line, current_dir):
    """
    Архивирует папки с расширением tar
    :param command_line: список, где находятся файлы для архивации
    :param current_dir: строка, в которой записана текущая директория
    :return: Возвращает результат выполнения функции: успех или ошибка
    """
    if command_line:
        for file in command_line:
            try:
                shutil.make_archive(str(os.path.join(current_dir, file)), 'tar', str(os.path.join(current_dir, file)))
            except FileNotFoundError:
                print('Каталог не найден')
                return 'Каталог не найден'
            except NotADirectoryError:
                print('Передан не каталог')
                return 'Передан не каталог'
        return 'Success'
    else:
        print('Недостаточно аргументов для команды')
        return 'Недостаточно аргументов для команды'
