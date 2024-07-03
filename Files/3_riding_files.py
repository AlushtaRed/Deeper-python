# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.
def riding_files(names, nums):
    with open(names, 'r', encoding='utf-8') as names, open(nums, 'r', encoding='utf-8') as nums, open('result.txt', 'w', encoding='utf-8') as result:
        list_names = names.readlines()
        list_nums = nums.readlines()
        list_names = list(map(lambda x: x.strip(), list_names))
        list_nums = list(map(lambda x: int(x.strip().split(
            '|')[0]) * float(x.strip().split('|')[1]), list_nums))
        print(list_names, list_nums)
        result_list = list(zip(list_names,list_nums))
        print(result_list)
        for st in result_list:
            if st[1]>0:
                result.write(f'{st[0].upper()} -> {round(st[1])}\n')
            else:
                result.write(f'{st[0].lower()} -> {abs(st[1])}\n')

riding_files('names.txt', 'nums.txt')
