def roll(lev, num):
    global L
    if lev == L:
        print(*dice)
        return
    for n in range(num,7):
        dice[lev] = n
        roll(lev+1, n)

L = int(input())
dice = [0] * L
roll(0, 1)