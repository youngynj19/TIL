N = int(input())
path = [0]*101

def f(n):
    if path[n] > 0:
        return path[n]
    
    if n == 1:
        path[1] = 1
    elif n == 2:
        path[2] = 2
    else:
        path[n] = f(n-2)*f(n-1)%100
    return path[n]

print(f(N))