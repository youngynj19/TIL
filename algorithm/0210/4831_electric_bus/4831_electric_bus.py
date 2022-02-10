# 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
# 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다.


import sys
sys.stdin = open('sample_input.txt')

# 움직일 수 있는 거리만큼 가보고 거기에 있으면 굿(남은거리까지..깔까?)
# 없으면 그 전에 휴게소에서 충전
# 충전때마다 카운트 업뎃

T = int(input())

for tc in range(T):
    K, N, M = map(int, input().split())
    # K거리 == 충전없이 갈 수 있는 최장거리, N==노선길이, M==충전소개수
    gas_stat = list(map(int, input().split())) # 충전소 리스트

    bus_stat = 0 # 버스 현 위치
    i = -1 # 충전소 리스트의 인덱스..지금은 0번째 충전소에 있는게 아니니까
    counts = 0 # 충전 횟수
    last_gas = 0 # 이전 충전소 위치
    while bus_stat + K < N: # 현재거리에서 K거리만큼 간 지점에 종착역이 없으면
        ok = 0  # K거리 안에 주유소 있으면 True 넣을 생각

        # 이전 지점에서 K거리까지 더 간 지점에 충전소가 있다면
        if last_gas + K in gas_stat :
            bus_stat += K # 개꿀
            ok = 1 # K거리 안에 주유소 있다^^
        else: # K거리에 없으면 일단 찾아가야지

            # 이 다음 충전소부터 끝까지 살펴볼꺼야
            # ...사실 K거리까지만 살펴보고싶은데 어떻게 하는지 모름
            for j in range(i+1, M):
                if gas_stat[j]-last_gas > K:
                    # K 넘어가는 충전소까지 살펴보는건 무의미하니까 break
                    break
                bus_stat = gas_stat[j] # K 넘어가지 않는 범위내에 있으면 업뎃
                ok = 1 # K거리 안에 주유소 있다^^...
                # ok = 1 없이 위에 break 걸렸으면 while문도 빠이

        if ok == 0: # K거리 안에 주유소 없으면 while문 나가셈
            counts = 0
            break

        i = gas_stat.index(bus_stat) # 주유소 위치 인덱스 업뎃
        last_gas = bus_stat # 이전 주유소 업뎃(...i로 표현 가능???)
        counts += 1

    print(f'#{tc+1} {counts}')
#1 3
#2 0
#3 4


#이재준, 홍성목
#오하민