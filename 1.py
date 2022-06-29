def f(a,b,c):
    mx,md,mn = a,a,a

    if b > a:
        mx = b
    else:
        md = b

    if c>a and c>b:
        mx,md,mn = c,mx,md
    elif c>a or c>b:
        md,mn = c, md
    else:
        mn = c

    print(int(mx*10//10+1),int(mn*10//10),int((md+0.5)*10//10))

a,b,c = map(float, input().split())
f(a,b,c)

# mx, mn, md = 0,0,0
# if a >= b:
#     if c>=a:
#         mx, md, mn = c,a,b
#     elif b>=c:
#         mx, md, mn = a,b,c
#     else:
#         mx,md,mn = a,c,b
# elif c>=b:
#     mx, md,mn = c,b,a
# elif a>=c:
#     mx,md,mn = b,a,c
# else:
#     mx,md,mn = b,c,a