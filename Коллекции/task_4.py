# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.
my_list = [1,2,3,4,5,6,7,8,9,1,3,5,7,9,2]


cnt_dict = {}
for i in my_list:
    cnt_dict[i] = cnt_dict.get(i, 0)+1

for key,value in cnt_dict.items():
    if value == 2:
        my_list.remove(key)
        my_list.remove(key)

# count_dict = {}
# for item in my_list:
#     count_dict[item] = count_dict.get(item, 0) + 1

# my_list_copy = my_list[:]

# for i in range(len(my_list_copy)):
#     if count_dict[my_list_copy[i]] == 2:
#         my_list.remove(my_list_copy[i])


print(cnt_dict)
print(my_list)