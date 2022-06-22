lst = list(input().split())
n = int(input())
dic = dict()
for name in lst:
    if name in dic:
        dic[name] += 1
    else:
        dic.update({name: 1})
for name in lst:
    a = dic.get(name)
    if a == n:
        print(name)
        dic.pop(name)