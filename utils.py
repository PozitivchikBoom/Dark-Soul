def g(z):
    i = 5
    s = 1
    while i != abs(z):
        i = i*5
        s += 1
    return s

def f(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * f(n - 1)
