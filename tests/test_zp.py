import os
from unittest.mock import patch
from src.archive_commands.zp import zip_folder
class TestZp:

    def test_zip_no_arguments(self):
        """Тест: rm без аргументов должен завершиться с ошибкой"""
        s = ''
        result = zip_folder([], s)
        assert result == 'Недостаточно аргументов для команды'


    def test_create_zp_archive(self, fs):
        """Тест: создаем zip архив из папки"""
        current_dir = '/testdir'
        src_dir = 'test'
        fs.create_dir(current_dir)
        test_dir_path = os.path.join(current_dir, src_dir)
        fs.create_dir(test_dir_path)
        test_file_path = os.path.join(test_dir_path, 'file.txt')
        fs.create_file(test_file_path, contents='Test content')
        result = zip_folder([src_dir], current_dir)
        assert result == 'Success'
        assert os.path.exists('/testdir/test.zip')


    def test_create_more_than_one_archives(self, fs):
        """Тест: пробуем заархивировать сразу несколько директорий"""
        current_dir = '/testdir'
        src_dir1 = 'test1'
        src_dir2 = 'test2'
        src_dir3 = 'test3'
        fs.create_dir(current_dir)
        test_dir_path1 = os.path.join(current_dir, src_dir1)
        test_dir_path2 = os.path.join(current_dir, src_dir2)
        test_dir_path3 = os.path.join(current_dir, src_dir3)
        fs.create_dir(test_dir_path1)
        fs.create_dir(test_dir_path2)
        fs.create_dir(test_dir_path3)
        test_file_path1 = os.path.join(test_dir_path1, 'file.txt')
        test_file_path2 = os.path.join(test_dir_path2, 'file.txt')
        test_file_path3 = os.path.join(test_dir_path3, 'file.txt')
        fs.create_file(test_file_path1, contents='Test content')
        fs.create_file(test_file_path2, contents='Test content')
        fs.create_file(test_file_path3, contents='Test content')
        result = zip_folder([src_dir1, src_dir2, src_dir3], current_dir)
        assert result == 'Success'
        assert os.path.exists('/testdir/test1.zip')
        assert os.path.exists('/testdir/test2.zip')
        assert os.path.exists('/testdir/test3.zip')


    def test_file_doesnt_exist(self, fs):
        """Тест: архивируемый файл не существует"""
        current_dir = '/testdir/'
        fs.create_dir(current_dir)
        with patch('src.archive_commands.zp.print') as mock_print:
            result = zip_folder(['notexist'], current_dir)
            assert result == 'Каталог не найден'
            mock_print.assert_called_once_with('Каталог не найден')


    def test_file_archive(self, fs):
        """Тест: пытаемся заархивировать файл"""
        current_dir = '/testdir'
        src_dir = 'test'
        fs.create_dir(current_dir)
        test_dir_path = os.path.join(current_dir, src_dir)
        fs.create_dir(test_dir_path)
        test_file_path = os.path.join(test_dir_path, 'file.txt')
        fs.create_file(test_file_path, contents='Test content')
        result = zip_folder([test_file_path], current_dir)
        assert result == 'Передан не каталог'










