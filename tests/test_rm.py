import shutil
import pytest
from src.rm import rm
import os.path
from src.constants import PROJECT_DIR


def test_rm_existing():
    res = rm('1213'.split())
    assert res == 'Такой файл не найден'




def test_rm_directory():
    res = rm((str(os.path.join(PROJECT_DIR, 'tests')) + ' ' + str(os.path.join(PROJECT_DIR, 'src'))).split())
    assert res == 'Для удаления папки используйте -r'