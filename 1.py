def f(a,b):
    a,b = a**(1/2), b**(1/2)
    mn,mx = min(a,b), max(a,b)
    a,b = int(mn*10//10+1), int(mx*10//10)

    print(b-a+1)

a,b = map(float, input().split())
f(a,b)