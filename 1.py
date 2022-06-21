lst = [100]
lst.append(int(input()))
for i in range(100):
    n = lst[i] - lst[i+1]
    lst.append(n)
    if n < 0:
        break
print(*lst)