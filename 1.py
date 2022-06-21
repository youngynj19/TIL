lst = list(input().split())
count = list(0 for _ in range(30))
for c in lst:
    count[ord(c)-65] += 1

for i in range(30):
    if count[i] != 0:
        print(f'{chr(i+65)} : {count[i]}')