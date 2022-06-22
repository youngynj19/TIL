lst = [[1 for _ in range(5)] for i in range(5)]
for i in range(5):
    for j in range(5):
        if i*j:
            lst[i][j] = lst[i][j-1] + lst[i-1][j]
        print(lst[i][j], end=' ')
    print()