def g(z):
    i = 5
    s = 1
    while i != abs(z):
        i = i*5
        s += 1
    return s
z = int(input())
print(g(z))