def f(n):
    if n < 10:
        return n**2

    return (n%10)**2 + f(n//10)

print(f(int(input())))