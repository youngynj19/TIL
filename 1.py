n = 0
lst = []

while True:
    c = input()
    if c == '0':
        break
    if "mo" in c:
        lst.append(c)
    n += 1
print(n)
for c in lst:
    print(c)