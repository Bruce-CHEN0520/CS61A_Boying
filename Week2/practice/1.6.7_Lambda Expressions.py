def compose1(f, g):
    return lambda x: f(g(x))

"     lambda            x            :          f(g(x))"
"A function that    takes x    and returns     f(g(x))"

def f(x):
    return x+1

def g(x):
    return x*x


f1_lambda = compose1(f,g)
print(f1_lambda(2))

s = lambda x: x * x
print(s(12))

compose2 = lambda f,g: lambda x: f(g(x))
print(compose2)
f2_lambda = compose2(f,g)
print(f2_lambda)
print(f2_lambda(2))
