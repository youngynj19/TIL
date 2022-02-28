import sys
from pprint import pprint
sys.stdin = open("input.txt")

def DFS(i):
    stack = []
    visited[i] = 1
    print(i, end=' ')
    while i != 0:
        for w in range(1, V+1):
            if G[i][w] == 1 and visited[w] == 0:
                stack.append(w)
                i = w
                visited[i] = 1
                print(i, end=' ')
                break
        else:
            if stack:
                i = stack.pop()
            else:
                i = 0
    return


V, E = map(int, input().split())
data = list(map(int, input().split()))

G = [[0 for _ in range(V+1)] for _ in range(V+1)]

visited = [0] * (V+1)

for i in range(E):
    G[data[i * 2]][data[i * 2 + 1]] = 1
    G[data[i * 2 + 1]][data[i * 2]] = 1

pprint(G)
print('='*30)
DFS(1)
