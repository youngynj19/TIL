def f(lst):
    n1 = int(lst[0])
    n2 = int(lst[2])
    opr = lst[1]
    opr_lst = ['+', '-', '*', '/']
    ans_lst = [n1+n2, n1-n2, n1*n2, n1//n2]
    for i in range(4):
        if opr == opr_lst[i]:
            return ans_lst[i]
    return 0

lst = list(input().split())

print(*lst, f'= {f(lst)}')