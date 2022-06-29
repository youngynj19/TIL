def f(n):
    global N
    if n == N:
        return
    print("recursive")
    f(n+1)

N = int(input())
f(0)