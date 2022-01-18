
num = int(input("type: "))
num_ref = num
num_pre = num
total = 0


for i in range(0, 10):
    print("{0}".format(i), end = '')
print('')
    
for j in range(0, 10):
    if j == (num_ref % 10):
        total += 1
    while num > 0:
        if num == int(num_pre / 10):
            num_pre = num
            if j == (num_pre % 10):
                total += 1
            #print("if - j= %d, t= %d, n= %d, n_p= %d" %(j, total, num, num_pre))
        num -= 1
        #print("while - j= %d, t= %d, n= %d, n_p= %d" %(j, total, num, num_pre))
    print(total, end ='')
    num_pre = num_ref
    num = num_ref
    total = 0
