k = int(input())

n = 64
for i in range(k, 0, -1):
    for _ in range(i):
        n += 1
        print(chr(n),end='')
    print()