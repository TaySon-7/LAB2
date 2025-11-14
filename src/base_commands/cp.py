import os
import shutil
from src.advanced_commands.undo import undo_history


def cp(command_line: list) -> str:
    """
    Копирует файл в папку или создает такой ж, но с другим именем
    :param command_line: список, где находится путь к копируемому файлу или каталогу, путь назначения
    :return: Возвращает результат выполнения функции: успех или ошибка
    """
    flag = False
    if command_line[0] == '-r':
        flag = True
        command_line.pop(0)
    if len(command_line) == 2:
        src = command_line[0]
        dst = command_line[1]
        if flag:
            try:
                os.path.isdir(dst)
                dst = str(os.path.join(dst, os.path.basename(src)))
                shutil.copytree(src, dst, dirs_exist_ok=True)
                undo_history(f'cp {flag} "{os.path.abspath(dst)}"')
                return 'Success'
            except NotADirectoryError:
                print('Для рекурсивного копирования каталога один путь не каталог')
                return 'Для рекурсивного копирования каталога один путь не каталог'
        else:
            try:
                shutil.copy(command_line[0], command_line[1])
                dr, fl = os.path.split(src)
                undo_history(f'cp {flag} "{os.path.join(os.path.abspath(dst), fl)}"')
                return 'Success'
            except IsADirectoryError:
                print('Каталог нельзя копировать нерекурсивно')
                return 'Каталог нельзя копировать нерекурсивно'
            except FileNotFoundError:
                print('Файл не найден')
                return 'Файл не найден'
    else:
        print("Должны быть введены стартовый путь и путь назначения")
        return "Должны быть введены стартовый путь и путь назначения"