import os
import fitz
from docx import Document


def cat(command_line: list) -> str:
    """
    Функция выполянет вывод содержимого файла на экран пользоавтеля
    :param command_line: список содержащий файлы, которые требуется вывести на экран
    :return: Возвращает результат выполнения функции: успех или ошибка
    """
    for path in command_line:
        try:
            if path.lower().endswith('.pdf'):
                with fitz.open(path) as file_pdf:
                    print("\n".join(page.get_text() for page in file_pdf))
            elif path.lower().endswith('.docx'):
                file_word = Document(path)
                print("\n".join(p.text for p in file_word.paragraphs))
            else:
                file = open(path, 'r').read()
                print(file)
        except FileNotFoundError:
            print('Такого файла не существует')
            return 'Такого файла не существует'
        except IsADirectoryError:
            print('Данный путь директория, а не файл')
            return 'Данный путь директория, а не файл'
    return 'Success'


