
def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total
sum_naturals(100)

def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k*k*k, k + 1
    return total
sum_cubes(100)

def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / ((4*k-3) * (4*k-1)), k + 1
    return total
pi_sum(100)

def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def cube(x):
    return x*x*x
def identity(x):
    return x

def sum_cubes(n):
    return summation(n, cube)

def sum_naturals(n):
    return summation(n, identity)


def improve_to_golden_value(close, update, guess = 1):
    while not close(guess):
        guess = update(guess)
    return guess

def square_close_to_successor(x):
    return approx_eq(x * x, x + 1)

def approx_eq(x,y, tolerance = 1e-3):
    return abs(x - y) < tolerance

def golden_update(x):
    return 1 /x + 1

pre_golden_guess =1
print (pre_golden_guess)
golden_value = improve_to_golden_value(square_close_to_successor, golden_update)
print(golden_value)

