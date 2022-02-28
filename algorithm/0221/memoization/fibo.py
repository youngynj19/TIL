import sys
sys.setrecursionlimit(3000)

def fibo(n):
    global cnt
    cnt += 1
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

n = 2000
cnt = 0
memo = [0] * (n+1)
memo[0], memo[1] = 0, 1
print(fibo(n))
print(cnt)
# 30 -> 832040