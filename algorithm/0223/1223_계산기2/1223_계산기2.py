import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    N = int(input())
    string = input()
    stack = [None] * 5
    i = 0

    new_str = ''
    for chr in string:
        if i == 0:
            if chr in ['+', '*']:
                stack[i] = chr
                i += 1
            else:
                new_str += chr
        else:
            if chr == '+':
                if i == 2:
                    stack[i-1] = None
                    new_str += '*+'
                    i -= 1
                else:
                    new_str += stack[i-1]
                    stack[i-1] = chr
            elif chr == '*':
                if stack[i-1] == '*':
                    new_str += '*'
                else:
                    stack[i] = '*'
                    i += 1
            else:
                new_str += chr
    for i in range(4,-1,-1):
        if stack[i] != None:
            new_str += stack[i]

    i = 0
    for chr in new_str:
        if chr not in ['+', '*']:
            stack[i] = int(chr)
            i += 1
        elif chr == '+':
            stack[i-2] += stack[i-1]
            stack[i-1] = None
            i -= 1
        else:
            stack[i-2] *= stack[i-1]
            stack[i-1] = None
            i -= 1

    print(f'#{tc} {stack[0]}')