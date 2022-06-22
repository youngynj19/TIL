def compare(i1, i2):
    c1, c2 = lst[i1], lst[i2]
    i = 0
    while i<len(c1) and i<len(c2):
        if ord(c1[i]) < ord(c2[i]):
            return
        elif ord(c2[i]) < ord(c1[i]):
            lst[i1], lst[i2] = c2, c1
        i += 1
    if len(c1) > len(c2):
        lst[i1], lst[i2] = c2, c1

lst = list(input().split())
s = set(lst)
lst = list(s)
l = len(lst)
for i in range(l-1, 0, -1):
    for j in range(i):
        compare(j, j+1)
print(*lst)
print(l)