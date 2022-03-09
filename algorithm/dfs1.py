# 연결요소의 크기 구하기
# => 방문처리가 몇번 되는지 센다.


n, m = map(int, input().split())
v = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)


visited = [False for i in range(n + 1)]
cnt = 0

def dfs(cur):
    global cnt

    visited[cur] = True
    cnt += 1

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        dfs(nxt)

dfs(1)

print(cnt - 1)

