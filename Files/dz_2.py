# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

# Создайте файл __init__.py и запишите в него функцию rename_files

import os



with open('__init__.py', 'w', encoding='utf-8') as file:
    file.write(f"from dz_1 import rename_files\n")
    file.write('\n')
    file.write(f"__all__ = ['rename_files']\n")

with open("__init__.py", "r") as init_file:
    code = init_file.read()
    print(code)
    print(type(code))