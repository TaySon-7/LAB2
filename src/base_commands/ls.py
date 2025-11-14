import os
import stat
import pwd
import grp
import time


def ls(command_line: list) -> str:
    option = False
    paths = []

    # Обработка опций
    if command_line and command_line[0] == '-l':
        option = True
        command_line = command_line[1:]

    # Определение путей для обработки
    if command_line:
        paths = command_line
    else:
        paths = [os.getcwd()]

    # Обработка каждого пути
    for path in paths:
        try:
            if not os.path.exists(path):
                print(f'Такого пути не существует: {path}')
                return 'Такого пути не существует'

            files = sorted(os.listdir(path))

            for file in files:
                file_path = os.path.join(path, file)
                if option:
                    st = os.lstat(file_path)
                    laws = stat.filemode(st.st_mode)
                    user_name = pwd.getpwuid(st.st_uid).pw_name
                    group_name = grp.getgrgid(st.st_gid).gr_name
                    size_file = st.st_size
                    time_file = time.strftime("%Y-%m-%d %H:%M", time.localtime(st.st_mtime))
                    print(f'{laws} {user_name} {group_name} {size_file} {time_file} {file}')
                else:
                    print(file)

        except PermissionError:
            print(f'Нет доступа к данной директории: {path}')
            return 'Нет доступа к данной директории'
        except Exception as e:
            print(f'Ошибка при обработке {path}: {e}')
            return 'Ошибка'

    return 'Success'