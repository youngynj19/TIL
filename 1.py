def f(n, i):
    global N
    if n == 0:
        print(1)
        return

    if i == N:
        print(n)
        return
    else:
        f(n*i, i+1)

N = int(input())

f(N, 1)