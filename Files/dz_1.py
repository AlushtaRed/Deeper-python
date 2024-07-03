import os
print(os.listdir())
list_dir = os.listdir()
for i in list_dir:
    if os.path.isfile(i):
        print(i)