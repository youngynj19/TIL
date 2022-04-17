'''
input
8 9
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 1 8

output
1 2 4 6 5 7 3 8
'''
from pprint import pprint

def DFS(v):
    stack = []
    visited[v] = 1
    print(v, end=' ')
    # print(v, visited)
    while v != 0:  # True:
        for w in range(1, V + 1):
            if G[v][w] == 1 and visited[w] == 0:
                stack.append(v)  # 방문 경로 저장
                v = w
                # print(v, visited)
                visited[w] = 1
                print(w, end=' ')
                break
        else:  # 다음 정점이 없으면
            if stack:
                v = stack.pop()  # 지나온 정점이 남아있는 경우
            else:
                v = 0  # 지나온 정점이 남아있지 않은 경우
                # break
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