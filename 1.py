nums = [0 for _ in range(7)]
dice = list(map(int, input().split()))
for n in dice:
    nums[n] += 1
for i in range(1,7):
    print(f'{i} : {nums[i]}')