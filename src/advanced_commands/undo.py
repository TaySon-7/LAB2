from src.base.constants import UNDO_HISTORY_FILE
import os
import shutil
import shlex


def undo() -> str:
    """
    Отменяет последнюю из введенных пользователем команд типа: cp, rm, mv
    :return: Возвращает результат выполнения функции: успех или ошибка
    """
    res = False
    with open(os.path.abspath(UNDO_HISTORY_FILE), 'r') as f:
        ln = list(f.readlines())
        if len(ln) == 0:
            print('Не было команд для их отмены')
            return 'Не было команд для их отмены'
        line = shlex.split(ln[-1])
        ln.pop(-1)
        if line[1] == 'cp':
            try:
                if line[2] == 'False':
                    os.remove(line[3])
                    res = True
                if line[2] == 'True':
                    shutil.rmtree(line[3])
                    res = True
            except FileNotFoundError:
                print('файл не найден')
                return 'файл не найден'
        elif line[1] == 'rm':
            dr, file = os.path.split(line[4])
            print(line[3], dr)
            try:
                dr, file = os.path.split(line[4])
                print(line[3], dr)
                shutil.move(line[3], dr)
                res = True
            except FileNotFoundError:
                print('файл не найден')
                return 'файл не найден'
        elif line[1] == 'mv':
            if line[2] == 'MOVE':
                try:
                    dr, file = os.path.split(line[3])
                    shutil.move(os.path.join(line[4], file), dr)
                except FileNotFoundError:
                    print('файл не найден')
                    return 'файл не найден'
            elif line[2] == 'RENAME':
                try:
                    os.rename(line[4], line[3])
                except FileNotFoundError:
                    print('файл не найден')
                    return 'файл не найден'

    if res:
        with open(os.path.abspath(UNDO_HISTORY_FILE), 'w') as f:
            f.writelines(ln)
            return 'Success'
    return 'Ошибка'


def undo_history(command):
    mx = 33
    with open(os.path.abspath(UNDO_HISTORY_FILE), 'r') as f:
        ln = list(f.readlines())
        new_ln = []
        if len(ln) == mx:
            ln.pop(0)
            for line in range(len(ln)):
                com = " ".join(ln[line].split()[1:])
                new_ln.append(str(line + 1) + ' ' + com)
            new_ln.append(str(mx) + ' ' + command)
        else:
            new_ln = [line.replace('\n', '') for line in ln]
            new_ln.append(str(len(ln) + 1) + ' ' + command)
    with open(os.path.abspath(UNDO_HISTORY_FILE), 'w') as f:
        f.write('\n'.join(new_ln))