import os
import pytest
from unittest.mock import patch
from src.advanced_commands.grep import grep

class TestGrep:

    def test_grep_no_arguments(self):
        """Тест: grep без аргументов должен завершиться с ошибкой"""
        with pytest.raises(IndexError):
            grep([])


    def test_grep_file_search(self, fs):
        """Тест: поиск содержимого в файле"""
        src_file = '/test.txt'
        fs.create_file(src_file, contents='Data across the season\n of Sochi temperature degrees')
        with patch('src.advanced_commands.grep.print') as mock_print:
            result = grep(['Data', src_file])
            assert result == 'Success'
            mock_print.assert_called_once_with('/test.txt', 1, 'Data across the season\n')


    def test_grep_directory_search(self, fs):
        """Тест: поиск содержимого в директории"""
        current_dir = '/testdir'
        src_dir = 'test'
        fs.create_dir(current_dir)
        test_dir_path = os.path.join(current_dir, src_dir)
        fs.create_dir(test_dir_path)
        test_file_path = os.path.join(test_dir_path, 'file.txt')
        fs.create_file(test_file_path, contents='Data across the season\n of Sochi temperature degrees')
        with patch('src.advanced_commands.grep.print') as mock_print:
            result = grep(['-r', 'S', current_dir])
            assert result == 'Success'
            mock_print.assert_called_once_with('/testdir/test/file.txt', 2, ' of Sochi temperature degrees')


    def test_grep_directory_search_without_flag(self, fs):
        """Тест: попытка поиска в папке без флага -r"""
        current_dir = '/testdir'
        src_dir = 'test'
        fs.create_dir(current_dir)
        test_dir_path = os.path.join(current_dir, src_dir)
        fs.create_dir(test_dir_path)
        test_file_path = os.path.join(test_dir_path, 'file.txt')
        fs.create_file(test_file_path, contents='Data across the season\n of Sochi temperature degrees')
        with patch('src.advanced_commands.grep.print') as mock_print:
            result = grep(['S', current_dir])
            assert result == 'Success'
            mock_print.assert_called_once_with('/testdir/test - это папка внутри каталога, используйте рекурсивный поиск, '
 'либо каталог пустой')


    def test_grep_search_file_with_double_flag(self, fs):
        """Тест: поиск с опцией независимости регистра"""
        src_file = '/test.txt'
        fs.create_file(src_file, contents='Data across the season\n of Sochi temperature degrees')
        with patch('src.advanced_commands.grep.print') as mock_print:
            result = grep(['-i', 'S', src_file])
            assert result == 'Success'
            assert mock_print.call_count == 3


    def test_grep_search_file_nonexist(self):
        """Попытка поиска в несуществующем файле"""
        result = grep(['F1', 'nonexist'])
        assert result == 'Файл не существует'










