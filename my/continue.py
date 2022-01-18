nums = [1,2,3,4,5,6,7,8,9,10]
total = 0

for i in nums:
    if i % 3 == 0:
        continue
    total += i

print("total: {0}".format(total))