import pytest
from unittest.mock import patch, mock_open
from src.advanced_commands.history import history
from src.base.constants import MAX_VERSTAPPEN


class TestHistory:

    def test_history_mode_write_new_command(self):
        """Тест: запись новой команды в историю когда есть место"""
        with patch('src.advanced_commands.history.Path') as mock_path,\
            patch('src.advanced_commands.history.open', new_callable=mock_open) as mock_open_func:
                mock_open_func.return_value.__enter__.return_value.readlines.return_value = [
                    '1 ls\n',
                    '2 cd /home\n'
                ]
                mock_path.return_value = '/fake/history.txt'
                history('pwd', 'history')
                assert mock_open_func.call_count == 2
                mock_open_func.assert_any_call('/fake/history.txt', 'r')
                mock_open_func.assert_any_call('/fake/history.txt', 'w')
        write_handle = mock_open_func()
        write_calls = [call[0][0] for call in write_handle.write.call_args_list]
        written_content = ''.join(write_calls)
        assert '1 ls' in written_content
        assert '2 cd /home' in written_content
        assert '3 pwd' in written_content


    def test_history_mode_write_when_history_full(self):
        """Тест: запись когда история заполнена (MAX_VERSTAPPEN достигнут)"""
        with patch('src.advanced_commands.history.Path') as mock_path, \
                patch('src.advanced_commands.history.open', new_callable=mock_open) as mock_open_func:
                    full_history = [f'{i} command{i}\n' for i in range(1, MAX_VERSTAPPEN + 1)]
                    mock_open_func.return_value.__enter__.return_value.readlines.return_value = full_history
                    mock_path.return_value = '/fake/history.txt'
                    history('new_command', 'history')
                    write_handle = mock_open_func()
                    write_calls = [call[0][0] for call in write_handle.write.call_args_list]
                    written_content = ''.join(write_calls)
                    assert 'command1' != written_content[0]
                    assert '1 command2' in written_content
                    assert f'{MAX_VERSTAPPEN} new_command' in written_content


    def test_history_mode_command_display(self):
        """Тест: вывод истории на экран"""
        with patch('src.advanced_commands.history.Path') as mock_path, \
                patch('src.advanced_commands.history.open', new_callable=mock_open) as mock_open_func, \
                patch('src.advanced_commands.history.print') as mock_print:
                    history_content = [
                        '1 ls\n',
                        '2 cd /home\n',
                        '3 pwd\n'
                    ]
                    mock_open_func.return_value.__enter__.return_value.readlines.return_value = history_content
                    mock_path.return_value = '/fake/history.txt'
                    history('', 'command')
                    assert mock_print.call_count == 3
                    mock_print.assert_any_call('1 ls')
                    mock_print.assert_any_call('2 cd /home')
                    mock_print.assert_any_call('3 pwd')

