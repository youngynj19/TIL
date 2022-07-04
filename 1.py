lst = []
def f(n):
    if n == 1:
        lst.append(n)
        return
    
    lst.append(n)
    f(n//2)

f(int(input()))
print(*lst[::-1])