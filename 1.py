set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
lst = set1 - set2
lst = list(lst)

l = len(lst)
for i in range(l-1, 0, -1):
    for j in range(i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(*lst)