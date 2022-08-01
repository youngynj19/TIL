N = int(input())

def f(n, cnt):
    if n == 1:
        print(cnt)
        return
    
    if n%2:
        f(n//3, cnt+1)
    else:
        f(n//2, cnt+1)

f(N, 0)