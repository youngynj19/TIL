def f1(a1, a2):
    if abs(a1) > abs(a2):
        return a1
    else:
        return a2

def f2(a, b):
    if abs(a) < abs(b):
        return a
    else:
        return b

a, b = map(int, input().split())
print(f1(a, b))
c,d = map(float, input().split())
print(f2(c, d))