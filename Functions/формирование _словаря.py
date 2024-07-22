# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.
# text = '1 6'
def dict_unicode(text):
    result_dict = {}
    # text_list = sorted(text.split())
    text_list = sorted([int(i) for i in text.split()])

    # for i in range(min(text_list),max(text_list)+1):
    #     result_dict[chr(i)] = i
    return {chr(i): i for i in range(text_list[0], text_list[1]+1)}


print(dict_unicode('1013 1010'))
