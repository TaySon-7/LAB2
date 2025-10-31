import os
import stat
import pwd
import grp
import time


def ls(command_line: list) -> str:
    """
    Функция выводит содержимое текушей директории системы
    :param command_line: список, содержащий опцию -l и путь, где пользователь хочет увидеть содержимое
    :return: Возвращает результат выполнения функции: успех или ошибка
    """
    path = ''
    option = False
    flag = False
    if len(command_line) > 0:
        if command_line[0] == '-l':
            option = True
            command_line.pop(0)
    for path in command_line:
        flag = True
        files = ''
        try:
            os.path.exists(path)
            files = list(os.listdir(path))
        except FileNotFoundError:
            print('Такого файла не существует')
            return 'Такого файла не существует'
        except PermissionError:
            print('Нет доступа к данной директории')
            return 'Нет доступа к данной директории'

        for file in files:
            if option:
                st = os.lstat(os.path.join(path, file))
                laws = stat.filemode(st.st_mode)
                user_name = pwd.getpwuid(st.st_uid).pw_name
                group_name = grp.getgrgid(st.st_gid).gr_name
                size_file = st.st_size
                time_file = time.strftime("%Y-%m-%d %H:%M", time.localtime(st.st_mtime))
                print(f'{laws} {user_name} {group_name} {size_file} {time_file} {file}')
            else:
                print(file)
    if flag:
        return 'Success'
    current_dir = os.getcwd()
    files = list(os.listdir(current_dir))
    for file in files:
        if option:
            st = os.lstat(os.path.join(path, file))
            laws = stat.filemode(st.st_mode)
            user_name = pwd.getpwuid(st.st_uid).pw_name
            group_name = grp.getgrgid(st.st_gid).gr_name
            size_file = st.st_size
            time_file = time.strftime("%Y-%m-%d %H:%M", time.localtime(st.st_mtime))
            print(f'{laws} {user_name} {group_name} {size_file} {time_file} {file}')
        else:
            print(file)
    return 'Success'
