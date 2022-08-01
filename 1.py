N = int(input())

def f(n):
    if n == 1:
        return 0
    
    ans = 0
    if n%2:
        ans = f(n//3)
    else:
        ans = f(n//2)
    return ans+1

print(f(N))