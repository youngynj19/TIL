# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이 출력

import sys
sys.stdin = open('sample_input.txt')


T = int(input())

for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split())) # 주어진 숫자 리스트

    # max, min 에 하나씩 대입하면서 다음 값이랑 비교할 생각
    # 무조건 리스트 첫 번째 항으로 리셋 되게!
    maximum, minimum = 0, 1000001
    for number in numbers:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
    print(f'#{tc+1} {maximum-minimum}')

# #1 630739
# #2 740510
# #3 838110
