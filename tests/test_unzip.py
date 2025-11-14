import os
import pytest
from unittest.mock import patch
from src.archive_commands.unzip import unzip_folder
class TestUnzip:

    def test_unzip_no_arguments(self):
        """Тест: zip без аргументов должен завершиться с ошибкой"""
        s = ''
        result = unzip_folder([], s)
        assert result == 'Недостаточно аргументов для команды'


    def test_unzip_directory(self, fs):
        """Тест: создаем zip архив из папки"""
        current_dir = '/testdir'
        src_dir = 'test'
        fs.create_dir(current_dir)
        test_dir_path = os.path.join(current_dir, src_dir)
        fs.create_dir(test_dir_path)
        test_file_path = os.path.join(test_dir_path, 'file.txt')
        fs.create_file(test_file_path, contents='Test content')
        result = unzip_folder([src_dir], current_dir)
        assert result == 'Передан не zip файл'


    def test_unzip_zip_file(self, fs):
        """Тест: создаем zip архив из файла"""
        current_dir = '/testdir'
        src_dir = 'test'
        fs.create_dir(current_dir)
        test_dir_path = os.path.join(current_dir, src_dir)
        fs.create_dir(test_dir_path)
        test_file_path = os.path.join(test_dir_path, 'file.zip')
        fs.create_file(test_file_path, contents='Test content')
        with patch('src.archive_commands.unzip.shutil.unpack_archive') as mock_unpack:
            mock_unpack.return_value = None
            result = unzip_folder([test_file_path], current_dir)
            assert result == 'Success'
            mock_unpack.assert_called_once_with(filename='/testdir/test/file.zip', extract_dir='/testdir', format='zip')


    def test_unzip_nonexist_file(self, fs):
        """Тест: создаем zip архив из несуществующего файла"""
        current_dir = '/testdir'
        fs.create_dir(current_dir)
        with patch('src.archive_commands.unzip.shutil.unpack_archive') as mock_unpack:
            mock_unpack.side_effect = FileNotFoundError
            result = unzip_folder(['nonexist'], current_dir)
            assert result == 'Каталог не найден'
            mock_unpack.assert_called_once()


    def test_unzip_directory_2(self, fs):
        """Тест: создаем zip архив из папки с моком директории"""
        current_dir = '/testdir'
        fs.create_dir(current_dir)
        with patch('src.archive_commands.unzip.shutil.unpack_archive') as mock_unpack:
            mock_unpack.side_effect = IsADirectoryError
            result = unzip_folder([current_dir], current_dir)
            assert result == 'Передан каталог, не файл'
            mock_unpack.assert_called_once()












