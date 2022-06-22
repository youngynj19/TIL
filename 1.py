lst = [input().split() for _ in range(3)]
for i in range(3):
    for j in range(5):
        print(chr(ord(lst[i][j]) + 32), end=' ')
    print()