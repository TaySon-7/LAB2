import pytest
from unittest.mock import patch
from src.base_commands.cd import cd

class TestCd:

    def test_cd_no_arguments(self):
        """Тест: cd без аргументов должен вернуть ошибку переизбытка аргументов"""
        with patch('os.chdir') as mock_chdir:
            result = cd([])
            assert result == 'Success'
            mock_chdir.assert_not_called()


    def test_cd_too_many_arguments(self):
        """Тест: cd с слишком большим количеством аргументов должен вернуть ошибку"""
        with patch('os.chdir') as mock_chdir:
            result = cd(['dir1', 'dir2'])
            assert result == 'Переизбыток аргументов'
            mock_chdir.assert_not_called()


    def test_cd_home_directory(self):
        """Тест: cd ~ должен перейти в домашнюю директорию"""
        with patch('os.path.expanduser') as mock_expanduser,\
            patch('os.chdir') as mock_chdir:
            mock_expanduser.return_value = '/home/user'
            result = cd(['~'])
            mock_expanduser.assert_called_once_with('~')
            mock_chdir.assert_called_once_with('/home/user')
            assert result == 'Success'


    def test_cd_valid_directory(self):
        """Тест: cd с валидным путем должен успешно выполниться"""
        with patch('os.chdir') as mock_chdir:
            result = cd(['/valid/path'])
            mock_chdir.assert_called_once_with('/valid/path')
            assert result == 'Success'


    def test_cd_file_not_found(self):
        """Тест: cd с несуществующим путем должен вернуть ошибку"""
        with patch('os.chdir') as mock_chdir:
            mock_chdir.side_effect = FileNotFoundError()
            result = cd(['/nonexistent/path'])
            mock_chdir.assert_called_once_with('/nonexistent/path')
            assert result == 'Такого пути не существует'


    def test_cd_not_a_directory(self):
        """Тест: cd с путем к файлу должен вернуть ошибку"""
        with patch('os.chdir') as mock_chdir:
            mock_chdir.side_effect = NotADirectoryError()
            result = cd(['/path/to/file.txt'])
            mock_chdir.assert_called_once_with('/path/to/file.txt')
            assert result == 'Данный путь не является директорией'


    def test_cd_permission_error(self):
        """Тест: cd с путем без прав доступа должен вернуть ошибку"""
        with patch('os.chdir') as mock_chdir:
            mock_chdir.side_effect = PermissionError()
            result = cd(['/restricted/path'])
            mock_chdir.assert_called_once_with('/restricted/path')
            assert result == 'Недостаточно прав для просмотра данной директории'


    def test_cd_empty_string(self):
        """Тест: cd с пустой строкой должен обработаться как обычный путь"""
        with patch('os.chdir') as mock_chdir:
            cd([''])
            mock_chdir.assert_called_once_with('')
