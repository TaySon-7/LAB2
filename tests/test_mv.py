import pytest
from unittest.mock import patch
from src.base_commands.mv import mv

class TestMv:

    def test_mv_no_arguments(self):
        """Тест: cat без аргументов должен завершиться успешно"""
        result = mv([])
        assert result == 'Аргументов должно быть 2'


    def test_mv_file_not_exist(self):
        """ Тест: ошибка о не нахаождении файла"""
        with patch('src.base_commands.mv.os.path.exists') as mock_exists, \
                patch('src.base_commands.mv.print') as mock_print:
            mock_exists.return_value = False
            result = mv(['nonexist.txt', 'dst'])

            assert result == 'Первого файла не существует'
            mock_print.assert_called_once_with('Первого файла не существует')


    def test_mv_file_rename_success(self):
        """Тест: проверяет успешность переименования двух файлов"""
        with patch('src.base_commands.mv.os.path.exists') as mock_dst, \
            patch('src.base_commands.mv.os.rename') as mock_rename:
            mock_dst.return_value = False
            result = mv(['test1', 'test2'])
            mock_rename.assert_called_once_with('test1', 'test2')
            assert result == 'Success'
            mock_dst.assert_called_once_with('test2')


    def test_mv_file_rename_error(self):
        """Тест: проверяет успешность переименования двух файлов"""
        with patch('src.base_commands.mv.os.path.exists') as mock_dst, \
            patch('src.base_commands.mv.os.rename') as mock_rename:
            mock_dst.return_value = False
            mock_rename.side_effect = FileNotFoundError
            result = mv(['test1', 'test2'])
            mock_rename.assert_called_once_with('test1', 'test2')
            assert result == 'Первого файла не существует'
            mock_dst.assert_called_once_with('test2')


    def test_mv_exist_files(self):
        """Тест: с существующим первым файлом"""
        with patch("src.base_commands.mv.os.path.exists") as mock_dst, \
                patch('src.base_commands.mv.shutil.move') as mock_move:
            mock_dst.return_value = True
            result = mv(['test1.txt', 'dirtest'])
            mock_move.assert_called_once_with('test1.txt', 'dirtest')
            assert result == 'Success'


    def test_mv_exist_files_with_error(self):
        """Тест: с существующим первым файлом"""
        with patch("src.base_commands.mv.os.path.exists") as mock_dst, \
                patch('src.base_commands.mv.shutil.move') as mock_move:
            mock_dst.return_value = True
            mock_move.side_effect = FileNotFoundError
            result = mv(['test1.txt', 'dirtest'])
            mock_move.assert_called_once_with('test1.txt', 'dirtest')
            assert result == 'Первого файла не существует'
