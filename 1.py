def f(n, lst):
    for i in range(n-1,0,-1):
        for j in range(i):
            a,b = lst[j],lst[j+1]
            if a < b:
                lst[j], lst[j+1] = b,a

N = int(input())
lst = list(map(int, input().split()))

f(N, lst)