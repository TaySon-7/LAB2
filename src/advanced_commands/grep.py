import re
import os


def search(reg: compile, path: str) -> None:
    """
    Функция ищет совпадения с шаблоном регулярного выражения в строках файла
    :param reg: регулярное выражение
    :param path: путь к файлу
    :return:
    """
    try:
        with open(path,'r') as f:
            for num, line in enumerate(f, 1):
                if reg.search(line):
                    print(path, num, line)
    except FileNotFoundError:
        print(f'{path} - такого файла не существует')
    except UnicodeDecodeError:
        print(f'{path} - кодировка данного файла не поддерживается')
    except IsADirectoryError:
        print(f'{path} - это папка внутри каталога, используйте рекурсивный поиск, либо каталог пустой')
    except PermissionError:
        print(f'{path} - нет доступа к действию')


def search_dir(dir_path: str, reg: compile) -> None:
    """
    Функция рекурсивного поиска в каталоге
    :param dir_path: путь к папке
    :param reg: регулярное выражение
    :return:
    """
    for file in os.listdir(dir_path):
        path = os.path.join(dir_path, file)
        if os.path.isdir(path):
            search_dir(path, reg)
        if os.path.isfile(path):
            search(reg=reg, path=os.path.join(dir_path, file))


def grep(command_line: list) -> str:
    """
    Функция, которая ишет совпадения с запросом в строках файлов, указанных пользователем в пути назначения
    :param command_line: список, содержащий опции, регулярное выражение и путь назначения
    :return: Возвращает результат выполнения функции: успех или ошибка
    """
    flagr = False
    flagi = False
    for arg in command_line:
        if arg[0] == '-':
            if arg == '-ri' or arg == '-ir':
                flagr = True
                flagi = True
            if arg == '-r':
                flagr = True
            if arg == '-i':
                flagi = True
            command_line.pop(0)
        else:
            break
    pattern = command_line[0]
    command_line.pop(0)
    if flagi:
        reg = re.compile(pattern, re.IGNORECASE)
        print(32)
    else:
        reg = re.compile(pattern)
    for dir_file in command_line:
        if os.path.isdir(dir_file) and flagr:
            search_dir(dir_file, reg)
            return 'Success'
        elif os.path.isdir(dir_file):
            for file in os.listdir(dir_file):
                search(reg=reg, path=os.path.join(dir_file,file))
            return 'Success'
        elif os.path.isfile(dir_file):
            search(reg=reg, path=dir_file)
            return 'Success'
        else:
            print(f'{dir_file} - не существует')
            return 'Файл не существует'
    return 'Недостаточно аргументов для команды'
