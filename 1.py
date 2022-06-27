def f(n, lst):
    for i in range(n-1, 0, -1):
        for j in range(i):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(*lst)

n = int(input())
lst = list(map(int, input().split()))
f(n, lst)