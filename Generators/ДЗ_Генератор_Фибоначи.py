def fibonacci():
        first = 1
        second = 1
        for i in range(0,100):
            if i == 0:
                 yield i
            elif i == 2 or i == 1:
                yield 1
            else:
                fib = first+second
                first = second
                second = fib
                yield fib
f = fibonacci()
for i in range(22):
   print(next(f))