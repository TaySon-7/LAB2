from src.cd import cd
import os.path
from src.constants import PROJECT_DIR


def test_cd_existing():
    res = cd('1213'.split())
    assert res == 'Такого пути не существует'


def test_cd_file():
    res = cd(os.path.join(os.path.join(PROJECT_DIR, 'tests'),'test_ls.py').split())
    assert res == 'Данный путь не является директорией'


def test_cd_directory():
    res = cd(os.path.join(PROJECT_DIR, 'tests').split())
    assert res == 'Success'