tpl = (12, 3.45, 6, True, True, 'Строка')
print(tpl)
result = dict()
for item in tpl:
    if type(item) not in result:
        result[type(item)] = []
    result[type(item)].append(item)
print(result)
