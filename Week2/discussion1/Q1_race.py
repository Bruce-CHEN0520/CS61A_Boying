'''
Learning to use if and while is an essential skill. 
During this discussion, focus on what we've studied in the first three lectures: 
if, while, assignment (=), comparison (<, >, ==, ...), and arithmetic. 
Please don't use features of Python that we haven't discussed in class yet, such as for, range, and lists. 
We'll have plenty of time for those later in the course,
but now is the time to practice the use of if (textbook section 1.5.4) and while (textbook section 1.5.5). 

'''

def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes

result = race(5,7)
print(result)