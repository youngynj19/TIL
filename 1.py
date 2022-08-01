a,b,c = map(int, input().split())

def f(n):
    if n == 0:
        return 1

    ans = n%10 if n%10 else 1
    return f(n//10) * ans

print(f(a*b*c))