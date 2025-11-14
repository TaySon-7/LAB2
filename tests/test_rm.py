import os
import pytest
from unittest.mock import patch
from src.base.constants import TRASH_DIR
from src.base_commands.rm import rm

class TestRm:

    def test_rm_no_arguments(self):
        """Тест: rm без аргументов должен завершиться с ошибкой"""
        with pytest.raises(IndexError):
            rm([])


    def test_file_rm(self, fs):
        """Тест: удаление файла"""
        src_file = 'src/test.txt'
        fs.create_file(src_file)
        trash_dir = os.path.expanduser(TRASH_DIR)
        fs.create_dir(trash_dir)
        with patch('src.base_commands.rm.undo_history') as mock_undo:
            result = rm([src_file])
            assert result == 'Success'
            assert not(os.path.exists('src/test.txt'))
            mock_undo.assert_called_once_with('rm False "/Users/turevichmax/PycharmProjects/LAB2/.trash/src/test.txt" '
 '"/src/test.txt"')


    def test_directory_rm_with_yes(self, fs):
        """Тест: удаление директории при согласии пользователя"""
        src_dir = 'src/test'
        fs.create_dir(src_dir)
        trash_dir = os.path.expanduser(TRASH_DIR)
        fs.create_dir(trash_dir)
        with patch('src.base_commands.rm.undo_history') as mock_undo, \
            patch('src.base_commands.rm.input') as mock_input, \
            patch('src.base_commands.rm.print') as mock_print:
            mock_input.return_value = 'Y'
            result = rm(['-r', src_dir])
            assert result == 'Success'
            assert not(os.path.exists('src/test'))
            mock_undo.assert_called_once_with('rm True "/Users/turevichmax/PycharmProjects/LAB2/.trash/src/test" '
 '"/src/test"')
            mock_print.assert_called_once()


    def test_directory_rm_with_no(self, fs):
        """Тест: удаление директории при несогласии пользователя"""
        src_dir = 'src/test'
        fs.create_dir(src_dir)
        trash_dir = os.path.expanduser(TRASH_DIR)
        fs.create_dir(trash_dir)
        with patch('src.base_commands.rm.undo_history') as mock_undo, \
                patch('src.base_commands.rm.input') as mock_input, \
                patch('src.base_commands.rm.print') as mock_print:
            mock_input.return_value = 'N'
            result = rm(['-r', src_dir])
            assert result == 'Success'
            assert os.path.exists('src/test')
            mock_undo.assert_not_called()
            mock_print.assert_called_once()


    def test_rm_directory_without_flag(self, fs):
        """Тест: попытка удланеия папки без флага -r"""
        src_dir = 'src/test'
        fs.create_dir(src_dir)
        trash_dir = os.path.expanduser(TRASH_DIR)
        fs.create_dir(trash_dir)
        with patch('src.base_commands.rm.undo_history') as mock_undo, \
                patch('src.base_commands.rm.print') as mock_print, \
                patch('src.base_commands.rm.shutil.move') as mock_move:
            result = rm([src_dir])
            assert result == 'Для удаления папки используйте -r'
            assert os.path.exists('src/test')
            mock_undo.assert_not_called()
            mock_print.assert_called_once()
            mock_move.assert_not_called()


    def test_rm_file_with_flag(self, fs):
        """Тест: попытка удаления файла с флагом -r"""
        src_file = 'src/test.txt'
        fs.create_file(src_file)
        trash_dir = os.path.expanduser(TRASH_DIR)
        fs.create_dir(trash_dir)
        with patch('src.base_commands.rm.undo_history') as mock_undo, \
                patch('src.base_commands.rm.print') as mock_print, \
                patch('src.base_commands.rm.shutil.move') as mock_move:
            result = rm(['-r', src_file])
            assert result == 'Нельзя использовать -r для удаления файла'
            assert os.path.exists('src/test.txt')
            mock_print.assert_called_once()
            mock_undo.assert_not_called()
            mock_move.assert_not_called()





