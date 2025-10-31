import logging
from src.constants import LOG_FILE, DATAFORMAT

def setup_log() -> logging.Logger:
    """
    Функция создает логгер
    :return:
    """
    logger = logging.getLogger('log1.0')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(fmt='[%(asctime)s] %(levelname)s: %(message)s',
                                  datefmt=DATAFORMAT)
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
