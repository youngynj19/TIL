lst = [[5,8,10,6,4],[11,20,1,13,2],[7,9,14,22,3]]
for ls in lst:
    for n in ls:
        print(f'{n:>2}',end='   ')
    print()