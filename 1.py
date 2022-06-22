lst = list(map(int, input().split()))
for i in range(2, 10):
    lst.append((lst[i-1] + lst[i-2])%10)
print(*lst)