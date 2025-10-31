import os.path
from src.constants import PROJECT_DIR
import pytest
from src.ls import ls


def test_ls_existing():
    res = ls('1213.py'.split())
    assert res == 'Такого файла не существует'


def test_ls_file():
    with pytest.raises(NotADirectoryError):
        res = ls('test_ls.py'.split())
        assert res == 'Success'


def test_ls_directory():
    res = ls(os.path.join(PROJECT_DIR, 'tests', ).split())
    assert res == 'Success'

