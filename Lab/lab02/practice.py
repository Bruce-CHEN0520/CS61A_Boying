def f(x):
    if x == 0:
        return "zero"
    else:
        return ""
    
def sum_digits(x):
    total = x % 10
    #while x // 10 != 0:
    while x > 0:
        total = x % 10 + total
        x = x // 10
    return total

    # n > 0

    
boolean = lambda n, i: sum_digits(n * i) == 5

def count_condi(condition):
    def f(*arg):
        count = 0
        i = 1
        while i <= N:
            boolean = condition(*arg) 
            if boolean:
                count += 1 
            i += 1
        return count 
    return f


