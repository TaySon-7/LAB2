import pytest
from unittest.mock import patch, mock_open
from src.advanced_commands.undo import undo

class TestUndo:

    def test_undo_rename_correctly(self):
        """Тест: проверка вызова os.rename при отмене изменения имени"""
        with patch('src.advanced_commands.undo.os.path.abspath') as mock_path,\
            patch('src.advanced_commands.undo.open', new_callable=mock_open) as mock_open_func, \
            patch('src.advanced_commands.undo.os.rename') as mock_rename:
                mock_open_func.return_value.__enter__.return_value.readlines.return_value = [
                    '1 mv RENAME "/Users/turevichmax/PycharmProjects/LAB2/test1" "/Users/turevichmax/PycharmProjects/LAB2/test2"'
                ]
                mock_path.return_value = '/fake/history.txt'
                undo()
                assert mock_open_func.call_count == 1
                mock_open_func.assert_any_call('/fake/history.txt', 'r')
                mock_rename.assert_called_once_with('/Users/turevichmax/PycharmProjects/LAB2/test2',
 '/Users/turevichmax/PycharmProjects/LAB2/test1')


    def test_undo_mv_correctly(self):
        """Тест: проверка shutil.move при отмене перемещения файла"""
        with patch('src.advanced_commands.undo.os.path.abspath') as mock_path, \
                patch('src.advanced_commands.undo.open', new_callable=mock_open) as mock_open_func, \
                patch('src.advanced_commands.undo.shutil.move') as mock_move:
            mock_open_func.return_value.__enter__.return_value.readlines.return_value = [
                '12 mv MOVE "/Users/turevichmax/PycharmProjects/LAB2/test1.txt" "/Users/turevichmax/PycharmProjects/LAB2/dirtest"'
            ]
            mock_path.return_value = '/fake/history.txt'
            undo()
            assert mock_open_func.call_count == 1
            mock_open_func.assert_any_call('/fake/history.txt', 'r')
            mock_move.assert_called_once_with('/Users/turevichmax/PycharmProjects/LAB2/dirtest/test1.txt',
 '/Users/turevichmax/PycharmProjects/LAB2')


    def test_undo_rm_correctly(self):
        """Тест: проверка вызова shutil.move из trashdir для отмены удаления"""
        with patch('src.advanced_commands.undo.os.path.abspath') as mock_path, \
                patch('src.advanced_commands.undo.open', new_callable=mock_open) as mock_open_func, \
                patch('src.advanced_commands.undo.shutil.move') as mock_move:
            mock_open_func.return_value.__enter__.return_value.readlines.return_value = [
                '33 rm False "/Users/turevichmax/PycharmProjects/LAB2/.trash/test2.py" "/Users/turevichmax/Documents/test2.py"'
            ]
            mock_path.return_value = '/fake/history.txt'
            undo()
            mock_open_func.assert_any_call('/fake/history.txt', 'r')
            mock_move.assert_called_once_with('/Users/turevichmax/PycharmProjects/LAB2/.trash/test2.py',
 '/Users/turevichmax/Documents')


    def test_undo_cp_file_correctly(self):
        """Тест: проверка вызова os.remove при отмены копирвоания файла"""
        with patch('src.advanced_commands.undo.os.path.abspath') as mock_path, \
                patch('src.advanced_commands.undo.open', new_callable=mock_open) as mock_open_func, \
                patch('src.advanced_commands.undo.os.remove') as mock_remove:
            mock_open_func.return_value.__enter__.return_value.readlines.return_value = [
                '33 cp False "/Users/turevichmax/Documents/dir124/test3.txt"'
            ]
            mock_path.return_value = '/fake/history.txt'
            undo()
            mock_open_func.assert_any_call('/fake/history.txt', 'r')
            mock_remove.assert_called_once_with('/Users/turevichmax/Documents/dir124/test3.txt')


    def test_undo_cp_directory_correctly(self):
        """Тест: проверка вызова shutil.rmtree при отмене копирования директории"""
        with patch('src.advanced_commands.undo.os.path.abspath') as mock_path, \
                patch('src.advanced_commands.undo.open', new_callable=mock_open) as mock_open_func, \
                patch('src.advanced_commands.undo.shutil.rmtree') as mock_rmtree:
                    mock_open_func.return_value.__enter__.return_value.readlines.return_value = [
                        '33 cp True "/Users/turevichmax/Documents/dir124/test3"'
                    ]
                    mock_path.return_value = '/fake/history.txt'
                    undo()
                    mock_open_func.assert_any_call('/fake/history.txt', 'r')
                    mock_rmtree.assert_called_once_with('/Users/turevichmax/Documents/dir124/test3')




