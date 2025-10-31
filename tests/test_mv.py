import os.path
from src.constants import PROJECT_DIR
import pytest
from src.mv import mv


def test_mv_existing():
    res = mv('1213.py 123.py'.split())
    assert res == 'Первого файла не существует'





def test_mv_directory():
    res = mv(os.path.join(PROJECT_DIR, 'tests', ).split())
    assert res == 'Аргументов должно быть 2'