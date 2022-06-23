lst = list(input().split())

dic = dict()
for name in lst:
    if name in dic:
        dic[name] += 1
    else:
        dic.update({name: 1})

n = 0
for i in range(dic[lst[0]]+1):
    if i in dic.values():
        n = i
        break

for key, val in dic.items():
    if val == n:
        print(key)
print(n)