import sys
from src.base_commands.ls import ls
from src.base_commands.cd import cd
from src.base_commands.cat import cat
from src.base_commands.cp import cp
from src.base_commands.mv import mv
from src.base_commands.rm import rm
from src.base.logger import setup_log
import os
import shlex
from src.archive_commands.unzip import unzip_folder
from src.archive_commands.zp import zip_folder
from src.advanced_commands.grep import grep
from src.archive_commands.tar import tar_folder
from src.archive_commands.untar import untar_folder
from src.advanced_commands.history import history
from src.advanced_commands.undo import undo


def main() -> None:
    """
    Точка входа в приложение, обрабатывает и вызывает все команды, введенные пользователем
    :return: Данная функция ничего не возвращает
    """
    logger = setup_log()
    while sys.stdin:
        current_dir = os.getcwd()
        command_log = input(current_dir + " % ")
        command = command_log.split()
        key = command[0]
        if key == 'ls':
            logger.info(command_log)
            res = ls(command[1:])
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        elif key == 'cd':
            logger.info(command_log)
            res = cd(shlex.split(" ".join(command[1:])))
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        elif key == 'cat':
            logger.info(command_log)
            res = cat(shlex.split(" ".join(command[1:])))
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        elif key == 'cp':
            logger.info(command_log)
            res = cp(shlex.split(" ".join(command[1:])))
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        elif key == 'mv':
            logger.info(command_log)
            res = mv(shlex.split(" ".join(command[1:])))
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        elif key == 'rm':
            logger.info(command_log)
            res = rm(shlex.split(" ".join(command[1:])))
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        elif key == 'zip':
            logger.info(command_log)
            res = zip_folder(shlex.split(" ".join(command[1:])), current_dir=current_dir)
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        elif key == 'unzip':
            logger.info(command_log)
            res = unzip_folder(shlex.split(" ".join(command[1:])), current_dir=current_dir)
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        elif key == 'tar':
            logger.info(command_log)
            res = tar_folder(shlex.split(" ".join(command[1:])), current_dir=current_dir)
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        elif key == 'untar':
            logger.info(command_log)
            res = untar_folder(shlex.split(" ".join(command[1:])), current_dir=current_dir)
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        elif key == 'grep':
            logger.info(command_log)
            res = grep(shlex.split(" ".join(command[1:])))
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        elif key == 'history':
            logger.info(command_log)
            history('', mode='command')
            logger.info('success')
        elif key == 'undo':
            logger.info(command_log)
            res  = undo()
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        elif key == 'exit' or key == 'q' or key == 'quit':
            break
        else:
            print('Введена несуществующая команда')
    print('До встречи')
if __name__ == "__main__":
    main()
