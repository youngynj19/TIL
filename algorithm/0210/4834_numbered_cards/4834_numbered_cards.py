# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오.

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    cards = input() # 숫자카드 리스트
    # int로 바꾸고 리스트 넣고 넘 귀찮 걍 나중에 int로 바꿀께요

    # 카운팅 정렬에서 숫자별로 몇개 하는 그거 쓸...까...

    counts = [0]*10
    for num in cards:
        counts[int(num)] += 1 # int로 바꿔서 인덱스 계산

    # 최대값 구하는 프로그램 그~대로
    maximum = [10, -1] # [숫자, 빈도]
    for i in range(10):
        if counts[i] >= maximum[1]:
            # 같아도 업뎃, 그래야 동일 빈도에선 큰 숫자가 출력
            maximum = [i, counts[i]]

    print(f'#{tc+1} {maximum[0]} {maximum[1]}')