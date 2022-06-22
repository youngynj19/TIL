size, n = map(int, input().split())
lst = [i%n==0 for i in range(size)]
print(lst)