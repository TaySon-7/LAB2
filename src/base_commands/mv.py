import shutil
import os
from src.advanced_commands.undo import undo_history


def mv(command_line: list) -> str:
    """
    Функция перемещает указанный файл в путь назначения
    :param command_line: Список, где находится исходный файл и путь его перемещения
    :return: Возвращает результат выполнения функции: успех или ошибка
    """
    if len(command_line) == 2:
        res = ''
        src = command_line[0]
        dst = command_line[1]
        un_src = os.path.abspath(src)
        if os.path.exists(dst):
            try:
                shutil.move(src, dst)
                res = 'MOVE'
            except FileNotFoundError:
                print('Первого файла не существует')
                return 'Первого файла не существует'
        else:
            try:
                os.rename(src, dst)
                res = 'RENAME'
            except FileNotFoundError:
                print('Первого файла не существует')
                return 'Первого файла не существует'
        if res:
            undo_history(f'mv {res} "{un_src}" "{os.path.abspath(dst)}"')
            return 'Success'
        else:
            return 'Ошибка'
    else:
        print('Аргументов должно быть 2')
        return 'Аргументов должно быть 2'