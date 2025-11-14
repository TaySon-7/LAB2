import os.path


def cd(command_line: list) -> str:
    """
    Функция перемещает пользователя по введенному им пути к файлам и каталогам
    :param command_line: список, в котором находится путь назначения
    :return: Возвращает результат выполнения функции: успех или ошибка
    """
    if len(command_line) > 1:
        print('Переизбыток аргументов')
        return 'Переизбыток аргументов'
    try:
        if command_line:
            if command_line[0] == '~':
                path = os.path.expanduser('~')
            else:
                path = command_line[0]
            os.chdir(path)
    except FileNotFoundError:
        print('Такого пути не существует')
        return 'Такого пути не существует'
    except NotADirectoryError:
        print('Данный путь не является директорией')
        return 'Данный путь не является директорией'
    except PermissionError:
        print('Недостаточно прав для просмотра данной директории')
        return 'Недостаточно прав для просмотра данной директории'
    return 'Success'
