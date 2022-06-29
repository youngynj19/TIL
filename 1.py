def f(lst):
    for i in range(6, 3, -1):
        for j in range(i):
            a,b = lst[j],lst[j+1]
            if a>b:
                lst[j],lst[j+1]=b,a
    print(*lst)

f(list(map(int, input().split())))