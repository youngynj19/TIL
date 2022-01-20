dan = range(2, 10)
num = range(1, 10)

for i in dan:
    for k in num:
        print("{0} x {1} = {2:>2}".format(i, k, i*k))
        if k == 9:
            print()