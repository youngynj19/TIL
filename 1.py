n = int(input())
lst = [[0 for _ in range(n+1)] for _ in range(n)]
lst[0][1] = 1
for i in range(1,n):
    for j in range(1,n+1):
        lst[i][j] = lst[i-1][j-1] + lst[i-1][j]
        if lst[i][j] == 0:
            break

for i in range(n-1,-1, -1):
    for j in range(1,n+1):
        if lst[i][j] == 0:
            break
        print(lst[i][j],end=' ')
    print()