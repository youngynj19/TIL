def f(n):
    if n <= 0:
        return
    f(n-2)
    print(n, end=' ')

f(int(input()))