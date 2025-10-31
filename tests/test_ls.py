import pytest

from src.ls import ls
import os.path
from src.constants import PROJECT_DIR


def test_ls_existing():
    res = ls('1213'.split())
    assert res == 'Такого файла не существует'


def test_ls_file():
    with pytest.raises(NotADirectoryError):
        res = ls(os.path.join(os.path.join(PROJECT_DIR, 'tests'),'test_ls.py').split())
        assert res == 'Данный путь не является директорией'


def test_ls_directory():
    res = ls(os.path.join(PROJECT_DIR, 'tests').split())
    assert res == 'Success'