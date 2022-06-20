def compare(c1, c2):
    

lst = []
for _ in range(5):
    lst.append(input())

for i in range(4):
    for j in range(4-i):
        compare(lst[j], lst[j+1])

for c in lst:
    print(c)