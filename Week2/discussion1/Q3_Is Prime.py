def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    i,k = 1,0
    while (i <= n):
        if n % i == 0: 
            k = k+1
        i = i+1
    return not k - 2
'''0 is a false value and all other numbers are true values.'''
v = is_prime(4)
print(v)

assert is_prime(10) == False
assert is_prime(7) == True
