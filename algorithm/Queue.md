# Queue

#### 반복문으로 BFS 만들기

```python
import sys
sys.stdin = open('input.txt')

# 탐색 시작점
def BFS(v):
    # 방문 가능 지점 = 정점의 개수
    visited = [0]*(V+1)
    queue = []
    # 탐색 시작점
    queue.append(v)
    # 작업할 일이 남아 있는 동안
    while queue:
        # print(queue, end=' ')
        # queue의 첫 번째 원소 반환
        v = queue.pop(0)
        # 방문 하지 않았다면,
        if not visited[v]:
            visited[v] = True
            print('{} {}'.format(v, visited))
            for w in range(1, V+1):
                if G[v][w] == 1 and visited[w] == 0:
                    queue.append(w)


V, E = map(int, input().split())
data = list(map(int, input().split()))

G = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

for i in range(V + 1):
    '''
    G[data[0]][data[1]] = 1
    G[data[1]][data[0]] = 1

    G[data[2]][data[3]] = 1
    G[data[3]][data[2]] = 1
    '''
    G[data[i * 2]][data[i * 2 + 1]] = 1
    G[data[i * 2 + 1]][data[i * 2]] = 1

BFS(1)
```



#### BFS with recursion(재귀함수)

```python
import sys
sys.stdin = open('input.txt')

def bfs():
    # 큐가 비었으면 끝
    if not queue:
        return

    # 뽑아서
    v = queue.pop(0)

    # 방문 체크
    if not visited[v]: visited[v] = 1

    # 인접 체크
    for w in G[v]:
        # 방문 안했다면
        if not visited[w]:
            # queue에 넣자
            queue.append(w)

    bfs()


V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))

# Graph 초기화
G = [[] for _ in range(V + 1)]
# [[], [2, 3], [4, 5], [7], [6], [6], [7], []]
for i in range(len(temp) // 2):
    G[temp[i * 2]].append(temp[i * 2 + 1])

# 방문 표시 초기화
visited = [0] * (V + 1)

# bfs 탐색 시작
queue = [1]
bfs()

# 방문 확인
for visit, val in enumerate(visited):
    if val:
        print('{}'.format(visit), end='-')
```



#### BFS with size

```python
from collections import deque
import sys

def bfs(i):
    q = deque()
    visited[i] = True
    q.append(i)
    while len(q) >= 1:
        # size here!!!
        size = len(q)
        for _ in range(size):
        # to here!!!!
            i = q[0]
            q.popleft()
            print(i, end=' ')
            for ni in v[i]:
                if not visited[ni]:
                    visited[ni] = True
                    q.append(ni)

n, m = map(int, sys.stdin.readline().rstrip().split())
v = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    v[a].append(b)
    v[b].append(a)

visited = [False for i in range(n + 1)]

bfs(i)
```

