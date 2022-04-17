def DFS(v):
    stack = []
    visited[v] = 1
    print(v, end=' ')
    while v != 0:
        for w in range(1, V+1):
            if G[v][w] == 1 and not visited[w]:
                stack.append(v)
                v = w
                visited[w] = 1
                print(v, end=' ')
                break
        else:
            if stack:
                v = stack.pop()
            else:
                v = 0
    return



V, E = map(int, input().split())
data = list(map(int, input().split()))

G = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

visited = [0] * (V + 1)

for i in range(V + 1):
    '''
    G[data[0]][data[1]] = 1
    G[data[1]][data[0]] = 1

    G[data[2]][data[3]] = 1
    G[data[3]][data[2]] = 1
    '''
    G[data[i * 2]][data[i * 2 + 1]] = 1
    G[data[i * 2 + 1]][data[i * 2]] = 1
# pprint(G)
# print('=' * 30)
DFS(1)