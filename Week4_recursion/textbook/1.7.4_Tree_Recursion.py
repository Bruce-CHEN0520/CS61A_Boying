def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# 0 1 1 2 3 5
'''
fib(6) = 
fib(5) = fib(4) + fib(3) = fib(3) + fib(2) + fib(3) = 1 + 1 + 1 = 3
fib(4)  = fib(3) + fib(2) = 2
'''

