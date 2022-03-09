# dfs든 bfs든 한번 수행하면 출발한 노드에서 갈 수 있는 모든 노드를 방문


# 연결요소의 크기 구하기
# => 방문처리가 몇번 되는지 센다.


n = int(input())
m = int(input())
v = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)


visited = [False for i in range(n + 1)]

# cur번 노드부터 몇 개의 노드를 방문했는지 return
def dfs(cur):
    ret = 1

    visited[cur] = True

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        ret += dfs(nxt)

    return ret

print(dfs(1) - 1)