def f(n):
    idx = 0
    for i in range(n):
        for j in range(n):
            idx += 1
            print(idx, end=' ')
        print()

n = int(input())
f(n)