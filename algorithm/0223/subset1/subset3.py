def subset1(i, N, s, K, rs):
    global cnt
    cnt += 1
    if s == K:
        for j in range(N):
            if bit[j]:
                print(arr[j], end=' ')
        print()
    elif i == N:
        return
    elif s > K:
        return
    elif s+rs < K:
        return
    else:
        bit[i] = 1
        subset1(i+1, N, s + arr[i], K, rs-arr[i])
        bit[i] = 0
        subset1(i+1, N, s, K, rs-arr[i])

N = 10
K = 27
arr = [x for x in range(1, N+1)]
bit = [0]*N
cnt = 0
subset1(0, N, 0, K, sum(arr))
print(f'cnt: {cnt}')