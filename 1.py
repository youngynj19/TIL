lst = []
for i in range(3):
    lst.append(list(map(int, input().split())))
    lst[i] = set(lst[i])
print(f'Intersection: {lst[0]&lst[1]&lst[2]}')
print(f'Union: {lst[0]|lst[1]|lst[2]}')