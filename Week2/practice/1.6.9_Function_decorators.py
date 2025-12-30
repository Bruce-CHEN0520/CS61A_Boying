def trace(fn):
    def wrapped(x):
        print('-> ', fn, '(', x, ')')
        return fn(x)
    return wrapped

def inputf(x):
    return x + 1

wrappedf = trace(inputf)
result = wrappedf(1)
print(result)

@trace
def triple(x):
    return 3 * x