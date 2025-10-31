import sys
from src.ls import ls
from src.cd import cd
from src.cat import cat
from src.cp import cp
from src.mv import mv
from src.rm import rm
from src.logger import setup_log
import os
import shlex
from src.unzip import unzip_folder
from src.zp import zip_folder
from src.grep import grep
from src.tar import tar_folder
from src.untar import untar_folder
from src.history import history
from src.undo import undo


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
        if key == 'cd':
            logger.info(command_log)
            res = cd(shlex.split(" ".join(command[1:])))
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        if key == 'cat':
            logger.info(command_log)
            res = cat(shlex.split(" ".join(command[1:])))
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        if key == 'cp':
            logger.info(command_log)
            res = cp(shlex.split(" ".join(command[1:])))
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        if key == 'mv':
            logger.info(command_log)
            res = mv(shlex.split(" ".join(command[1:])))
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        if key == 'rm':
            logger.info(command_log)
            res = rm(shlex.split(" ".join(command[1:])))
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        if key == 'zip':
            logger.info(command_log)
            res = zip_folder(shlex.split(" ".join(command[1:])), current_dir=current_dir)
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        if key == 'unzip':
            logger.info(command_log)
            res = unzip_folder(shlex.split(" ".join(command[1:])), current_dir=current_dir)
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        if key == 'tar':
            logger.info(command_log)
            res = tar_folder(shlex.split(" ".join(command[1:])), current_dir=current_dir)
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        if key == 'untar':
            logger.info(command_log)
            res = untar_folder(shlex.split(" ".join(command[1:])), current_dir=current_dir)
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        if key == 'grep':
            logger.info(command_log)
            res = grep(shlex.split(" ".join(command[1:])))
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        if key == 'history':
            logger.info(command_log)
            history('', mode='command')
            logger.info('success')
        if key == 'undo':
            logger.info(command_log)
            res  = undo()
            if res == 'Success':
                logger.info('success')
                history(command_log, mode='history')
            else:
                logger.error(res)
        if key == 'exit' or key == 'q' or key == 'quit':
            break
    print('До встречи')
if __name__ == "__main__":
    main()
