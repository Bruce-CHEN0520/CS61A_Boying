def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10   
        return sum_digits(all_but_last) + last

assert sum_digits(123) == 6
assert sum_digits(11111) == 5
print(sum_digits(11408855402054064613470328848384))


'''
add gege digits from left to right
for example f(324234) = 3 + 2 + 4 + 2 + 3 + 4 = 18

123456 % 10
>>> 6
123456 // 10
>>> 12345

'''

