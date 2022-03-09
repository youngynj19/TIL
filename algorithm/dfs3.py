import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().rstrip().split())
v = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    v[a].append(b)
    v[b].append(a)

visited = [False for i in range(n + 1)]

def dfs(cur):
    visited[cur] = True

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        dfs(nxt)

cnt = 0
for i in range(1, n + 1):
    if visited[i]:
        continue

    cnt += 1
    dfs(i)

print(cnt)









