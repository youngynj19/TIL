lst = [list((i+1)%2 for i in range(5))] + [[0 for _ in range(5)] for _ in range(4)]
print(*lst[0])
for i in range(1,5):
    for j in range(5):
        a = lst[i-1][j-1] if 0<=j-1<=4 else 0
        b = lst[i-1][j+1] if 0<=j+1<=4 else 0
        lst[i][j] = a+b
        print(a+b,end=' ')
    print()