import os


def rename_files(desired_name: str, num_digits: int, source_ext: str, target_ext: str):
    list_dir = os.listdir()
    count = 1
    for i in list_dir:
        if os.path.isfile(i):
            if i.split('.')[1] == source_ext:
                # j = i.split('.')[0]
                digits = f'{'0'*(num_digits-1)}{count}'
                new_name = f'{desired_name}{
                          digits[-num_digits:]}.{target_ext}'
                os.rename(i, new_name)
                count += 1


rename_files('new', 5, 'doc', 'txt')
# rename_files(desired_name='new',num_digits=6, source_ext='txt', target_ext='doc')
# rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
