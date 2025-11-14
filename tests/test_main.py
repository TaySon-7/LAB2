import os
import pytest
from unittest.mock import patch, MagicMock, call
from src.base.main import main


class TestMain:

    def test_main_exit_commands(self):
        """Тест: команды выхода из программы"""
        exit_commands = ['exit', 'q', 'quit']
        for exit_cmd in exit_commands:
            with patch('src.base.main.input') as mock_input, \
                    patch('src.base.main.print') as mock_print:
                mock_input.side_effect = [exit_cmd]
                main()
                mock_print.assert_any_call('До встречи')


    def test_main_unknown_command(self):
        """Тест: обработка неизвестной команды"""
        with patch('src.base.main.input') as mock_input, \
                patch('src.base.main.print') as mock_print:
            mock_input.side_effect = ['unknown_command', 'exit']
            main()
            mock_print.assert_any_call('Введена несуществующая команда')


    def test_main_ls_success(self):
        """Тест: успешное выполнение команды ls"""
        with patch('src.base.main.input') as mock_input, \
                patch('src.base.main.ls') as mock_ls, \
                patch('src.base.main.history') as mock_history, \
                patch('src.base.main.os.getcwd') as mock_cwd:
            mock_input.side_effect = ['ls', 'exit']
            mock_ls.return_value = 'Success'
            mock_cwd.return_value = '/test/dir'
            main()
            mock_ls.assert_called_once_with([])
            mock_history.assert_called_once_with('ls', mode='history')


    def test_main_cd_success(self):
        """Тест: успешное выполнение команды cd"""
        with patch('src.base.main.input') as mock_input, \
                patch('src.base.main.cd') as mock_cd, \
                patch('src.base.main.history') as mock_history, \
                patch('src.base.main.os.getcwd') as mock_cwd:
            mock_input.side_effect = ['cd /home/user', 'exit']
            mock_cd.return_value = 'Success'
            mock_cwd.return_value = '/test/dir'
            main()
            mock_cd.assert_called_once()
            mock_history.assert_called_once_with('cd /home/user', mode='history')


    def test_main_multiple_commands(self):
        """Тест: выполнение нескольких команд подряд"""
        with patch('src.base.main.input') as mock_input, \
                patch('src.base.main.cp') as mock_cp, \
                patch('src.base.main.rm') as mock_rm, \
                patch('src.base.main.cat') as mock_cat, \
                patch('src.base.main.history') as mock_history, \
                patch('src.base.main.undo') as mock_undo, \
                patch('src.base.main.tar_folder') as mock_tar, \
                patch('src.base.main.untar_folder') as mock_untar, \
                patch('src.base.main.grep') as mock_grep, \
                patch('src.base.main.os.getcwd') as mock_cwd:
            mock_input.side_effect = ['cp test1.txt /dirtest', 'rm test1.txt',
                                      'cat file.txt', 'history', 'undo', 'tar /dirtest',
                                      'untar test.tar', 'grep A test.py','exit']
            mock_cp.return_value = 'Success'
            mock_rm.return_value = 'Success'
            mock_cat.return_value = 'Success'
            mock_grep.return_value = 'Success'
            mock_untar.return_value = 'Success'
            mock_undo.return_value = 'Success'
            mock_history.return_value = 'Success'
            mock_tar.return_value = 'Success'
            mock_cwd.return_value = '/test/dir'
            main()
            assert mock_cp.called
            assert mock_rm.called
            assert mock_cat.called
            assert mock_grep.called
            assert mock_untar.called
            assert mock_undo.called
            assert mock_history.called
            assert mock_tar.called
            assert mock_history.call_count == 8
            mock_history.assert_any_call('cp test1.txt /dirtest', mode='history')
            mock_history.assert_any_call('rm test1.txt', mode='history')
            mock_history.assert_any_call('cat file.txt', mode='history')
            mock_history.assert_any_call('undo', mode='history')
            mock_history.assert_any_call('tar /dirtest', mode='history')
            mock_history.assert_any_call('untar test.tar', mode='history')
            mock_history.assert_any_call('grep A test.py', mode='history')




