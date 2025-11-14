import pytest
from unittest.mock import Mock, patch
from pathlib import Path
from datetime import datetime
from src.base_commands.ls import ls

class TestLs:

    def setup_method(self):
        """Настройка перед каждым тестом - создаем экземпляр команды и тестовые данные"""
        self.cwd = Path("/tests/cwd")
        self.env = {}
        self.Ls = ls


    def test_ls_current_directory(self):
        """Тест: ls без аргументов должен показать содержимое текущей директории"""
        with patch('os.listdir') as mock_listdir, \
                patch('os.getcwd') as mock_getcwd, \
                patch('os.path.exists') as mock_path,\
                patch('builtins.print') as mock_print:
            mock_path.return_value = True
            mock_getcwd.return_value = '/tests/cwd'
            mock_listdir.return_value = ['file2.txt', 'file1.txt', 'abc.txt']
            result = self.Ls([])
            assert result == 'Success'
            expected_calls = ['abc.txt', 'file1.txt', 'file2.txt']
            actual_calls = [call_args[0][0] for call_args in mock_print.call_args_list]
            assert actual_calls == expected_calls


    def test_ls_current_directory_not_exist(self):
        """Тест: ls без аргументов должен показать содержимое текущей директории"""
        with patch('os.listdir') as mock_listdir, \
                patch('os.getcwd') as mock_getcwd, \
                patch('os.path.exists') as mock_path:
            mock_path.return_value = False
            mock_getcwd.return_value = '/tests/cwd'
            mock_listdir.return_value = ['file2.txt', 'file1.txt', 'abc.txt']
            result = self.Ls([])
            assert result == 'Такого пути не существует'


    def test_ls_with_path_argument(self):
        """Тест: ls с указанием пути должен показать содержимое указанной директории"""
        with patch('os.listdir') as mock_listdir, \
                patch('os.path.exists') as mock_exists, \
                patch('builtins.print') as mock_print:
            mock_exists.return_value = True
            mock_listdir.return_value = ['test.py']
            result = self.Ls(["src"])
            mock_listdir.assert_called_once_with("src")
            assert result == 'Success'
            mock_print.assert_called_once_with("test.py")


    def test_ls_long_format(self):
        """Тест: ls -l должен показать детальную информацию о файлах"""
        mock_file = Mock()
        mock_file.name = "test.py"
        mock_stat = Mock()
        mock_stat.st_mode = 0o100644
        mock_stat.st_uid = 1000
        mock_stat.st_gid = 1000
        mock_stat.st_size = 1024
        mock_stat.st_mtime = datetime(2023, 1, 1, 12, 0).timestamp()
        with patch('os.listdir') as mock_listdir, \
                patch('os.path.exists') as mock_exists, \
                patch('os.lstat') as mock_lstat, \
                patch('builtins.print') as mock_print:
            mock_exists.return_value = True
            mock_listdir.return_value = ['test.py']
            mock_lstat.return_value = mock_stat
            with patch('pwd.getpwuid') as mock_getpwuid, \
                    patch('grp.getgrgid') as mock_getgrgid, \
                    patch('time.strftime') as mock_strftime, \
                    patch('stat.filemode') as mock_filemode:
                mock_getpwuid.return_value = Mock(pw_name='testuser')
                mock_getgrgid.return_value = Mock(gr_name='testgroup')
                mock_strftime.return_value = '2023-01-01 12:00'
                mock_filemode.return_value = '-rw-r--r--'
                result = self.Ls(['-l'])
                assert result == 'Success'
                mock_lstat.assert_called_once()
                mock_print.assert_called_once_with('-rw-r--r-- testuser testgroup 1024 2023-01-01 12:00 test.py')