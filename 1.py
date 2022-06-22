scores = list(map(int, input().split()))
lst = [0 for i in range(11)]
for score in scores:
    lst[score//10] += 1

for i in range(10, -1, -1):
    if lst[i]:
        print(f'{i*10} : {lst[i]} person')