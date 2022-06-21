def compare(i1, i2):
    c1, c2 = lst[i1], lst[i2]
    idx = 0
    if idx<len(c1) and idx<len(c2):
        if ord(c1[idx]) > ord(c2[idx]):
            return
        elif ord(c1[idx]) < ord(c2[idx]):
            lst[i1], lst[i2] = c2, c1
            return
        idx += 1

    if len(c1) > len(c2):
        return
    else:
        lst[i1], lst[i2] = c2, c1
        return


lst = []

for _ in range(5):
    lst.append(input())

for i in range(4, 0, -1):
    for j in range(i):
        compare(j, j+1)

for i in range(5):
    print(lst[i])