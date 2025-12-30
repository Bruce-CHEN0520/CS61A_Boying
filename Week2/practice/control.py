def f(n):
    """Return the nth Fibonacci number.

    >>> f(8)
    13
    >>> f(9)
    21
        """
    # 0,1,1,2
    pred, curr = 0 , 1
    k = 2
    while (k<n):
        temp = pred
        pred = curr # pred = 1
        curr = temp + curr 
        k = k+1
       
        
    return curr

print(f(8))

def sum_naturals(n):
        """Return the sum of the first n natural numbers.

        >>> sum_naturals(10)
        55
        >>> sum_naturals(100)
        5050
        """
        total, k = 0, 1
        while k <= n:
            total, k = total + k, k + 1
        return total
from doctest import run_docstring_examples
run_docstring_examples(f, globals(), True)

h = 3
if h > 3:
    print('h >', 3)
elif h == 3:
    print('h = ',3)
else:
    print('h <', 3)

def add_sum(n):
    '''
    Docstring for add_sum
    
    :param k: Description
    '''
    total, k = 0, 1
    while (k <= n):
        total, k = total + k, k+1
    return total

print(add_sum(10))
## 1+2+3+4 = 10 


for _ in range(1,10,2):
    print(_) 

valuex = 0

assert valuex == 1
