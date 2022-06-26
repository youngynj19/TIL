'''
== 3dan ==
3 * 1 =  3
3 * 2 =  6
3 * 3 =  9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
'''

def f(n1, n2):
    if n2 < n1:
        n1, n2 = n2, n1

    for n in range(n1, n2 + 1):
        print(f'== {n}dan ==')
        for i in range(1,10):
            print(f'{n} * {i} = {n*i:>2}')
        print()

n1, n2 = map(int, input().split())

f(n1, n2)