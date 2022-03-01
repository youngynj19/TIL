'''
Q1
    else:
        subset1(i+1, N, K)
        bits[i] = 1
        subset1(i+1, N, K)
로 해도 되야할 것 같은데 안되는 이유는??
'''

def subset1(i, N, K):
    global cnt
    cnt += 1
    if i == N:
        s = 0
        for j in range(N):
            if bits[j]:
                s += arr[j]
        if s == K:
            for j in range(N):
                if bits[j]:
                    print(arr[j], end=' ')
            print()
    else:
        bits[i] = 1
        subset1(i+1, N, K)
        bits[i] = 0
        subset1(i+1, N, K)

N = 10
K = 10
cnt = 0
arr = [x for x in range(1, N+1)]
bits = [0] * N
subset1(0, N, K)
print(f'cnt: {cnt}')