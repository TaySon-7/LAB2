from shutil import SameFileError
import pytest
from src.cp import cp
import os.path
from src.constants import PROJECT_DIR


def test_cp_existing():
    res = cp('1213'.split())
    assert res == 'Должны быть введены стартовый путь и путь назначения'


def test_cp_file():
    with pytest.raises(SameFileError):
        res = cp('test_ls.py test_ls.py'.split())


def test_cp_directory():

    res = cp((str(os.path.join(PROJECT_DIR, 'tests')) + ' ' + str(os.path.join(PROJECT_DIR, 'src'))).split())
    assert res == 'Каталог нельзя копировать нерекурсивно'