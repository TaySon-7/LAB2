import os
import shutil
from src.advanced_commands.undo import undo_history
from src.base.constants import TRASH_DIR


def rm(command_line: list) -> str:
    """
    Функция удаляет файлы или папки
    :param command_line: список, где есть опция -r, папки и файлы для удаления
    :return: Возвращает результат выполнения функции: успех или ошибка
    """
    trash = os.path.expanduser(TRASH_DIR)
    flag = False
    if command_line[0] == '-r':
        flag = True
        command_line.pop(0)
    for file in command_line:
        if file == '/' or file == '..':
            print('Данные каталоги нельзя удалить')
            return 'Данные каталоги нельзя удалить'
        if flag:
            if os.path.isfile(file):
                print('Нельзя использовать -r для удаления файла')
                return 'Нельзя использовать -r для удаления файла'
            elif os.path.exists(file):
                    print('Ты уверен, что хочешь удалить всю папку? Введите y(Y)/n(N)')
                    fl = input()
                    if fl == 'y' or fl == 'Y':
                        shutil.move(file, trash)
                        undo_history(f'rm {flag} "{os.path.abspath(str(os.path.join(trash, file)))}" "{os.path.abspath(file)}"')
                        return 'Success'
                    elif fl == 'n' or fl == 'N':
                        return 'Success'
                    else:
                        print('Некорректный символ')
                        return 'Некорректный символ'
            else:
                print('Такого каталога не существует')
                return 'Такого каталога не существует'
        else:
            if os.path.isdir(file):
                print('Для удаления папки используйте -r')
                return 'Для удаления папки используйте -r'
            else:
                try:
                    shutil.move(file, trash)
                    undo_history(f'rm {flag} "{os.path.abspath(str(os.path.join(trash, file)))}" "{os.path.abspath(file)}"')
                    return 'Success'
                except FileNotFoundError:
                    print('Такой файл не найден')
                    return 'Такой файл не найден'

    print('Недостаточно аргументов для команды')
    return 'Недостаточно аргументов для команды'
