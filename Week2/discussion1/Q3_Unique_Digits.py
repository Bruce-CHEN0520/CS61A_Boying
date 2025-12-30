def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    un, i = 0, 0
    while (i < 10):
        if has_digit2(n,i):
            un = un + 1
        i = i + 1
    return un


'''
assert unique_digits(8675309) == 7
assert unique_digits(13173131) == 3
assert unique_digits(101) == 2 

'''


'''the way I can come up with right away is to store the number and frequency to a map, and then calculate the number of frequecny = 1 '''


def has_digit(n, k):
    """Returns whether k is a digit in n.
    
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    # compare every digit of n to k, if one of them is equal to k, return ture
    i = 0
    while(n >= 10**i):
        if (n % 10**(i+1)) // (10**i) == k:  # n = n//10
            return True
        i = i + 1
    return False

"""
def has_digit2(n, k):
    if n % 10 == k:
        return True
    
    while (n >= 10):
        n = n // 10
        if n % 10 == k:
            return True
    return False

"""

'''
print(10**0)
print(10**1)
print (0//1)
print (10 % 100 // 10)
print(has_digit(10,1))
print(has_digit(12,7)
'''

print(has_digit2(10,1))
print(has_digit2(12,7))
print(has_digit2(13,7))
print(has_digit2(15,5))
print(has_digit2(8675309,9))
print(has_digit2(8675309,0))

 
print(unique_digits(8675309))


assert unique_digits(8675309) == 7
assert unique_digits(13173131) == 3
assert unique_digits(101) == 2 

'''
>>> 18117 % 10
7
>>> 18117 // 10
1811
'''

