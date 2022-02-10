import sys
sys.stdin = open('sample_input.txt')

def diff(a, b): # 두 수의 차를 구하는 함수
    if a > b:
        return a-b
    else:
        return b-a

def my_sum(ls): # 리스트 원소의 합을 구하는 함수
    summ = 0
    for num in ls:
        summ += num
    return summ


T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    # M개씩 묶어서 나오는 수, 그 다음에 나오는 수 빼서 - 비교 후 max값 저장
    # or max, min 따로 구해서 바로 빼기 - 이게 나아보이지만 위에가 신박해서...
    max_diff = 0
    # 변수로 range를 만들 경우에는 머리 안굴러가니까 그냥 예시를 통해 계산해볼 것
    # 특히 20-19(-1) 같은 경우는 for문 안에 안들어가는 경우도 있으니까 주의!!!!!!!!!!!!!!!
    for j in range(N-M):
        first = my_sum(numbers[j:j+M]) # m까지 첫 번째 합
        for k in range(j+1, N-M+1):
            second = my_sum(numbers[k:k+M]) # 첫 번째 값 제외하고 다음 부터 합들
            if diff(first, second) > max_diff: # 두 합의 차가 더 크면 ㄱㄱ
                max_diff = diff(first, second)
    print(f'#{i+1} {max_diff}')




# import sys
# sys.stdin = open('sample_input.txt')
#
# T = int(input())
#
# for tc in range(T):
#     N, M = map(int, input().split())
#     numbers = list(map(int, input().split()))
#
#     max, min = 0, 10000*100
#     for i in range(N-M+1):
#         summation = 0
#         for j in range(i,i+M):
#             summation += numbers[j]
#         if summation > max:
#             max = summation
#         if summation < min:
#             min = summation
#     print(f'#{tc} {max-min}')





#1 21
#2 11088
#3 1090


# 근데 슬라이싱으로 해도 됨! 이중 for문 하지 말고