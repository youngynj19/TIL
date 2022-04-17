# 전위 중위 후위
n = int(input())
lft = {}
rgt = {}
for i in range(n):
    a, b, c = map(str, input().split())

    lft[a] = b
    rgt[a] = c

# print(lft)
# print(rgt)
def dfs(c, opt):
    if c == '.':
        return
    
    if opt == 0:
        print(c, end='')
    dfs(lft[c], opt)
    if opt == 1:
        print(c, end='')
    dfs(rgt[c], opt)
    if opt == 2:
        print(c, end='')

dfs('A', 0)
print()
dfs('A', 1)
print()
dfs('A', 2)