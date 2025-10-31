from src.cat import cat
import os.path
from src.constants import PROJECT_DIR


def test_cat_existing():
    res = cat('1213.py'.split())
    assert res == 'Такого файла не существует'


def test_cat_file():
    res = cat(os.path.join(os.path.join(PROJECT_DIR, 'tests'),'test_ls.py').split())
    assert res == 'Success'


def test_cat_directory():
    res = cat(os.path.join(PROJECT_DIR, 'tests').split())
    assert res == 'Данный путь директория, а не файл'