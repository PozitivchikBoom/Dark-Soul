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
      

def parny(file):
    counter = 0
    for el in file:
        if float(el) % 2 == 0:
            counter += 1
    return counter

def kvadrat(file): #b
    counter = 0
    for n in file:
        if float(n) == (int(float(n)**0.5))**2 and float(n) % 2 != 0:
            counter += 1
    return counter