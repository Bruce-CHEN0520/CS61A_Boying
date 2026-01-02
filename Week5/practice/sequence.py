type(2)

# pairs
pair1 = [10, 20]
from operator import getitem
getitem(pair1, 0)

digits = [1,8,2,8]
x,y,z,i = digits
print(x)
print(y)

def rational(n, d):
    return [n, d]

def numer(x):
    return x[0]

def denom(x):
    return x[1]

def add_rationals(x,y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)
# three layers: 

def mul_rationals(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def square_rational_violating_once(x):
    return rational(numer(x) * numer(x), denom(x) * denom(x))

def square_rational_violating_twice(x):
    return [x[0] * x[0], x[1] * x[1]]

def pair(x, y):
    def get(index):
        if index == 0:
            return x
        if index == 1:
            return y
    return get

new_pair = pair(1,2)

def select(p, i):
    return p(i)

p = pair(20, 14)
select(p,0)