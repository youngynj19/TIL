print('first array')
lst1 = [list(map(int, input().split())) for i in range(2)]
print('second array')
lst2 = [list(map(int, input().split())) for i in range(2)]
for i in range(2):
    for j in range(4):
        print(lst1[i][j]*lst2[i][j],end=' ')
    print()