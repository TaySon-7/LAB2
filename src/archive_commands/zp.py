import os.path
import shutil


def zip_folder(command_line: list, current_dir: str) -> str:
    """
    Функция создает архив из папки с расширением zip
    :param command_line: список из папок к архивации
    :param current_dir: строка с путём текущей директории
    :return: Возвращает результат выполнения функции: успех или ошибка
    """
    if command_line:
        for file in command_line:
            try:
                shutil.make_archive(str(os.path.join(current_dir, file)), 'zip', str(os.path.join(current_dir, file)))
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
