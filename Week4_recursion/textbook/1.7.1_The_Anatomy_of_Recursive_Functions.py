'''
Docstring for Week4_recursion.1.7.1_The_Anatomy_of_Recursive_Functions

4! = 4 * 3 * 2 * 1 
'''
def fact_iter(n):
    total, k = 1, 1
    while (k <= n):
        total, k = total*k, k+1
    return total


def fact(n):
    if n == 1:
        return n 
    else:
        total, n = n, n-1
        return fact(n) * total
    
    
def fac2(n):
    if n == 1:
        return n 
    else:
        return n * fact(n-1)

print(fact(3))
print(fact(4))


      
