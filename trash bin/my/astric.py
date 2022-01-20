i, k = 5, 1

while i > 0:
    print("{0}{1}".format(" " * i, '*' * (2*k-1)))
    i -= 1
    k += 1