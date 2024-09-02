# def func1():
#     return [i for i in range(10)]
# res = func1()

# for el in res:
#     print(el)

def func2():
    return (i for i in range(10))

res2 = func2()
for el in res2:
    print(el)
res2 = func2()
for el in res2:
    print(el)