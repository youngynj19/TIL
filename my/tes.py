# 정수 N값 초기화
N = 0

# 정수 받기
while 1:
    N = int(input("1 ~ 1,000 정수 입력: "))
    if 1 <= N <= 1000:
        break

# N의 약수 오름차순 출력
for i in range(1, N+1):
    if N % i == 0:
        print(i, end=' ')