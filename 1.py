n = 0
lst = ["flower", "rose", "lily", "daffodil", "azalea"]
c = input()

for ch in lst:
    if ch[1] == c or ch[2] == c:
        print(ch)
        n += 1
print(n)