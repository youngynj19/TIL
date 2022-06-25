def f(n, m):
    ans = 1
    for _ in range(m):
        ans *= n
    return ans

n, m = map(int, input().split())

print(f(n, m))