from pathlib import Path
from src.constants import HISTORY_FILE

def history(command: str, mode: str) -> None:
    """
    Функция сохраняет и выводит историю введенных команд по запросу пользователя
    :param command: строка с последней введенной пользователем командой
    :param mode: запись истории или вывод её пользователю
    :return:
    """
    mx = 33
    if mode == 'history':
        with open(Path(HISTORY_FILE), 'r') as f:
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
        with open(Path(HISTORY_FILE), 'w') as f:
            f.write('\n'.join(new_ln))
    if mode == 'command':
        with open(Path(HISTORY_FILE), 'r') as f:
            ln = f.readlines()
            for line in ln:
                line = line.replace("\n", '')
                print(line)
