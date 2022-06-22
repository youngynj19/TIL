lst = [[3, 5, 9],

[2, 11, 5],

[8, 30, 10],

[22, 5, 1]]
print(sum(sum(lst[i]) for i in range(4)))