n = int(input())
lst = list(map(int, input().split()))

for i in range(n-1):
    for j in range(n-1-i):
        if lst[j] < lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

for i in range(n):
    print(lst[i])