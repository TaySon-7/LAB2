import os
import pytest
from unittest.mock import patch
from src.base_commands.cp import cp

class TestCp:

    def test_cp_no_arguments(self):
        """Тест: cp без аргументов должен завершиться с ошибкой"""
        with pytest.raises(IndexError):
            cp([])


    def test_cp_file_to_directory(self, fs):
        """Тест: сокпируем файл в директорию """
        src_file = '/src/file.txt'
        fs.create_file(src_file, contents='test content')
        dest_dir = '/dest/'
        fs.create_dir(dest_dir)
        with patch('src.base_commands.cp.undo_history') as mock_undo:
            cp([src_file, dest_dir])
            mock_undo.assert_called()
            assert os.path.exists('/dest/file.txt')
            with open('/dest/file.txt', 'r') as f:
                assert f.read() == 'test content'


    def test_cp_directories(self, fs):
        """Тест: сокпируем директорию в директорию """
        src_dest = '/src/test'
        fs.create_dir(src_dest)
        dest_dir = '/dest/'
        fs.create_dir(dest_dir)
        with patch('src.base_commands.cp.undo_history') as mock_undo:
            cp(['-r', src_dest, dest_dir])
            mock_undo.assert_called()
            assert os.path.exists('/dest/test')


    def test_cp_not_existing_file(self, fs):
        """Тест: попробуем скопировать не существующий файл"""
        src_dst = '/dest/'
        fs.create_dir(src_dst)
        result = cp(['notexist12342', src_dst])
        with patch('src.base_commands.cp.undo_history') as mock_undo:
            mock_undo.assert_not_called()
            assert result == 'Файл не найден'


    def test_cp_wrong_flag(self, fs):
        """Тест: скопируем файл с флагом -r"""
        src_file = 'src/test.txt'
        dest_dir = '/dest/'
        fs.create_file(src_file)
        fs.create_dir(dest_dir)
        result = cp(['-r', src_file, dest_dir])
        with patch('src.base_commands.cp.undo_history') as mock_undo:
            mock_undo.assert_not_called()
            assert result == 'Для рекурсивного копирования каталога один путь не каталог'


    def test_cp_directory_without_flag(self, fs):
        """Тест: скопируем папку без флага -r"""
        src_dir = 'src/test'
        dest_dir = '/dest/'
        fs.create_dir(src_dir)
        fs.create_dir(dest_dir)
        result = cp([src_dir, dest_dir])
        with patch('src.base_commands.cp.undo_history') as mock_undo:
            mock_undo.assert_not_called()
            assert result == 'Каталог нельзя копировать нерекурсивно'


