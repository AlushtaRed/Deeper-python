# Напишите функцию get_file_info, которая принимает
# на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов:
# путь, имя файла, расширение файла.

file_path = "file_in_current_directory.txt"


def get_file_info(file_path = str):
    if '/' in file_path:
        temp_text = file_path.split('/')
        path = '/'.join(temp_text[:-1]) + '/'
        name = temp_text[-1].split('.')[:-1]
        name = '.'.join(name)
        extention = '.'+temp_text[-1].split('.')[-1]
        print((path, name, extention))
        return path, name, extention
    else:
        temp_text = file_path.split('/')
        path = '/'.join(temp_text[:-1])
        name = temp_text[-1].split('.')[:-1]
        name = '.'.join(name)
        extention = '.'+temp_text[-1].split('.')[-1]
        print((path, name, extention))
        return path, name, extention

get_file_info(file_path)
# print(get_file_info(file_path))
