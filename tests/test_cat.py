import pytest
from unittest.mock import patch, mock_open, MagicMock
from src.base_commands.cat import cat

class TestCat:

    def test_cat_no_arguments(self):
        """Тест: cat без аргументов должен завершиться успешно"""
        result = cat([])
        assert result == 'Success'


    def test_cat_text_file_success(self):
        """Тест: вывод содержимого текстового файла"""
        test_content = "Hello World\nTest Content"
        with patch('src.base_commands.cat.open', mock_open(read_data=test_content)):
            with patch('src.base_commands.cat.print') as mock_print:
                result = cat(['test.txt'])
                assert result == 'Success'
                mock_print.assert_called_once_with(test_content)


    def test_cat_pdf_file_success(self):
        """Тест: вывод содержимого PDF файла"""
        with patch('src.base_commands.cat.fitz.open') as mock_fitz:
            mock_page = MagicMock()
            mock_page.get_text.return_value = "PDF Content"
            mock_doc = MagicMock()
            mock_doc.__enter__.return_value = [mock_page]
            mock_fitz.return_value = mock_doc
            with patch('src.base_commands.cat.print') as mock_print:
                result = cat(['document.pdf'])
                assert result == 'Success'
                mock_print.assert_called_once_with("PDF Content")


    def test_cat_docx_file_success(self):
        """Тест: вывод содержимого docx файла"""
        with patch('src.base_commands.cat.Document') as mock_docx:
            mock_paragraph = MagicMock()
            mock_paragraph.text = "DOCX Content"
            mock_doc = MagicMock()
            mock_doc.paragraphs = [mock_paragraph]
            mock_docx.return_value = mock_doc
            with patch('src.base_commands.cat.print') as mock_print:
                result = cat(['document.docx'])
                assert result == 'Success'
                mock_print.assert_called_once_with("DOCX Content")


    def test_cat_file_not_found(self):
        """Тест: обработка несуществующего файла"""
        with patch('src.base_commands.cat.open', side_effect=FileNotFoundError()):
            with patch('src.base_commands.cat.print') as mock_print:
                result = cat(['nonexistent.txt'])
                assert result == 'Такого файла не существует'
                mock_print.assert_called_once_with('Такого файла не существует')


    def test_cat_is_directory(self):
        """Тест: обработка попытки чтения директории"""
        with patch('src.base_commands.cat.open', side_effect=IsADirectoryError()):
            with patch('src.base_commands.cat.print') as mock_print:
                result = cat(['/some/directory'])
                assert result == 'Данный путь директория, а не файл'
                mock_print.assert_called_once_with('Данный путь директория, а не файл')


    def test_cat_multiple_files(self):
        """Тест: обработка нескольких файлов"""
        test_content1 = "First File"
        test_content2 = "Second File"
        with patch('src.base_commands.cat.open') as mock_file:
            mock_file.side_effect = [
                mock_open(read_data=test_content1).return_value,
                mock_open(read_data=test_content2).return_value
            ]
            with patch('src.base_commands.cat.print') as mock_print:
                result = cat(['file1.txt', 'file2.txt'])
                assert result == 'Success'
                # Проверяем что оба файла были напечатаны
                assert mock_print.call_count == 2
                mock_print.assert_any_call(test_content1)
                mock_print.assert_any_call(test_content2)
