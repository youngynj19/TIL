def f(n):
    if n == 8:
        print()
        return
    print(2*n+1,end=' ')
    f(n+1)
    print(2*n+1, end=' ')

# lst = [3, 5, 7, 9, 11, 15]

f(1)