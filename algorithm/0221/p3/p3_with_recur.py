import sys
sys.stdin = open('input.txt')

def DFS(n):
    visited[n] = 1
    print(n, end=' ')

    for w in range(1, V+1):
        if ways[n][w] == 1 and visited[w] == 0:
            DFS(w)

V, E = map(int, input().split())
data = list(map(int, input().split()))

ways = [[0 for _ in range(V+1)] for _ in range(V+1)]

visited = [0] * (V + 1)

for i in range(E):
    ways[data[i*2]][data[i*2+1]] = 1
    ways[data[i*2+1]][data[i*1]] = 1

DFS(1)