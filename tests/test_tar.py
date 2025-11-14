import os
import pytest
from unittest.mock import patch
from src.archive_commands.tar import tar_folder

class TestTar:

    def test_tar_no_arguments(self):
        """Тест: tar без аргументов должен завершиться с ошибкой"""
        current_dir = '/testdir'
        result = tar_folder([], current_dir)
        assert result == 'Недостаточно аргументов для команды'


    def test_create_tar_archive(self, fs):
        """Тест: создаем tar архив из папки с моком shutil"""
        current_dir = '/testdir'
        src_dir = 'test'
        fs.create_dir(current_dir)
        test_dir_path = os.path.join(current_dir, src_dir)
        fs.create_dir(test_dir_path)
        test_file_path = os.path.join(test_dir_path, 'file.txt')
        fs.create_file(test_file_path, contents='Test content')
        with patch('src.archive_commands.tar.shutil.make_archive') as mock_make_archive:
            mock_make_archive.return_value = None
            result = tar_folder([src_dir], current_dir)
            assert result == 'Success'
            expected_archive_path = os.path.join(current_dir, src_dir)
            mock_make_archive.assert_called_once_with(
                expected_archive_path, 'tar', expected_archive_path
            )


    def test_create_more_than_one_archives(self, fs):
        """Тест: заархивировать несколько директорий"""
        current_dir = '/testdir'
        src_dirs = ['test1', 'test2', 'test3']
        fs.create_dir(current_dir)
        for src_dir in src_dirs:
            test_dir_path = os.path.join(current_dir, src_dir)
            fs.create_dir(test_dir_path)
            test_file_path = os.path.join(test_dir_path, 'file.txt')
            fs.create_file(test_file_path, contents='Test content')
        with patch('src.archive_commands.tar.shutil.make_archive') as mock_make_archive:
            mock_make_archive.return_value = None
            result = tar_folder(src_dirs, current_dir)
            assert result == 'Success'
            assert mock_make_archive.call_count == 3
            for src_dir in src_dirs:
                expected_path = os.path.join(current_dir, src_dir)
                mock_make_archive.assert_any_call(expected_path, 'tar', expected_path)


    def test_file_doesnt_exist(self, fs):
        """Тест: архивируемый файл не существует"""
        current_dir = '/testdir'
        fs.create_dir(current_dir)
        with patch('src.archive_commands.tar.shutil.make_archive') as mock_make_archive:
            mock_make_archive.side_effect = FileNotFoundError
            result = tar_folder(['notexist'], current_dir)
            assert result == 'Каталог не найден'


    def test_file_archive(self, fs):
        """Тест: пытаемся заархивировать файл вместо директории"""
        current_dir = '/testdir'
        fs.create_dir(current_dir)
        test_file_path = os.path.join(current_dir, 'file.txt')
        fs.create_file(test_file_path, contents='Test content')
        with patch('src.archive_commands.tar.shutil.make_archive') as mock_make_archive:
            mock_make_archive.side_effect = NotADirectoryError
            result = tar_folder(['file.txt'], current_dir)
            assert result == 'Передан не каталог'

