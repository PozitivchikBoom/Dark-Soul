def g(z):
    i = 5
    s = 1
    while i != abs(z):
        i = i*5
        s += 1
    return s
z = int(input())
print(g(z))

def parny(file):
    counter = 0
    for el in file:
        if float(el) % 2 == 0:
            counter += 1
    return counter