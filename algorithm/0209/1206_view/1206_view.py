# 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보
# 조망권이 확보된 세대의 수를 반환
# 총 10개의 테스트케이스가 주어진다.

import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input()) # 건물 갯수
    city = list(map(int, input().split())) # 건물 현황 int변환 후 list로 받기

    flat = 0 # 건물별 조망권 확보 가구수
    result = 0 # 총 조망권 확보 가구수
    for i in range(2, N-2): # 양 옆 0, 0 무시하기

        flat = city[i] - city[i-2] # 왼쪽 두 번째 건물과 비교
        for j in range(i-1, i+3): # 나머지 세개 건물이랑도 비교하는데
            if j == i: # 본인이랑은 비교 ㄴㄴ
                continue
            if city[i] - city[j] < flat: # 최소값을 flat에 저장
                flat = city[i] - city[j]

        if flat <= 0: # 근데 flat이 0보다 작다?;;
            flat = 0 # 응 0이야
        result += flat # 그리고 결과값에 더해주기

    print(f'#{tc+1} {result}')