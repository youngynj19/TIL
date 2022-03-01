def subset3(i, N, s, T, sr):
    global cnt
    cnt += 1
    if s == T:
        for j in range(N):
            if bit[j]:
                print(arr[j], end=' ')
        print()
    elif s > T:
        return
    elif s+sr < T:
        return
    elif i == N:
        return
    else:
        bit[i] = 1
        subset3(i+1, N, s + arr[i], T, sr - arr[i])
        bit[i] = 0
        subset3(i+1, N, s, T, sr - arr[i])

N = 10
T = 30
arr = [x for x in range(1, N+1)]
bit = [0] * N
cnt = 0
subset3(0, N, 0, T, sum(arr))
print(f'cnt: {cnt}')