def nums(a,b):
    return a**b

def my_func(*args):
    return args[0]**args[1]

def my_func1(a,b):
    return a**b

def my_func2(**kwargs):
    return kwargs['a']**kwargs['b']

func = lambda a,b: a**b

print(my_func2(b=4,a=4))
print((lambda a,b: a**b)(2,2))