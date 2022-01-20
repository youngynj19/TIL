```python
dan = int(input("단: "))
for i in range(1, 10, 1):
    print("{0} x {1} = {2:>2}" .format(dan, i, dan * i))

##################################################
    
dogs = {1: "골든리트리버", 2: "진", 3: "보"}

for key in dogs:
    print("{0} : {1}" .format(key, dogs[key]))

'''
for key, value in dogs.items():
    print("{0} : {1}" .format(key, value))
'''

#########################################33

str = "Python"

for c in str:
    print("{0}".format(c))
    
############################################333

scores = [100, 95, 88, 98]
total = 0

for score in scores:
    total += score

print("총점 : {0}".format(total))    

################################################33


for i in range(1, 5)
    print('*' * i)



