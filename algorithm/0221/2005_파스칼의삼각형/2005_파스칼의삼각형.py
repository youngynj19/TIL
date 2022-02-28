import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')

    pyramid = [[0]*N for _ in range(N)]
    pyramid[0][0] = 1
    print(pyramid[0][0])

    for i in range(1, N):
        for j in range(i+1):
            if j != 0:
                pyramid[i][j] = pyramid[i-1][j-1] + pyramid[i-1][j]
            else:
                pyramid[i][j] = 1
            print(pyramid[i][j], end=' ')
        print()