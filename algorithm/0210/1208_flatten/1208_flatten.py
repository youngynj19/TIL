import sys
sys.stdin = open('input.txt')


def sorting(input_arr):
    """
    input_arr : 입력 배열(1 to k)
    counting_arr : 카운트 배열
    k는 데이터의 개수가 아닌 데이터 원소의 범위
    """

    counting_arr = [0] * (100 + 1)

    # 1. counting array에 arr내 원소의 빈도수 담기
    for i in range(0, len(input_arr)):
        counting_arr[input_arr[i]] += 1
    # for i in input_arr:
    #     counting_arr[i] += 1

    # 2. 누적(counting_arr 업데이트)
    for i in range(1, len(counting_arr)):
        counting_arr[i] += counting_arr[i - 1]

    # 3. result_arr 생성
    result_arr = [-1] * len(input_arr)

    # 4. result_arr에 정렬하기(counting_arr를 참조)
    for i in range(len(result_arr) - 1, -1, -1):
        counting_arr[input_arr[i]] -= 1
        result_arr[counting_arr[input_arr[i]]] = input_arr[i]
    # for i in input_arr:
    #     counting_arr[i] -= 1
    #     result_arr[counting_arr[i]] = i

    return result_arr


# def sorting(bx): # 리스트 sort 함수
#     counts = [0]*101 # [0~100]까지 리스트 생성
#     new_counts = [0] * 101
#     for num in bx: # 숫자별 빈도 리스트 생성
#         counts[num] += 1
#     for i in range(101):
#         if i == 0:
#             continue
#         new_counts[i] = counts[i] + counts[i-1]
#         # 0 0 1 0 0 0 3 4 0 0 2
#         # 0 0 1 1 1 1 4 8 8 8 10
#     new_bx = list()
#     for num in bx:
#         # 박스의 값 -> 인덱스로 하는 counts의 값
#         # -> 의 '-1'을 인덱스로 하는 new boxes의 값에다가
#         # -> 박스의 값을 넣어준다, counts에서는 1 빼주고
#         counts[num] -= 1
#         new_bx[counts[num]] = num
#     return new_bx




for tc in range(10):
    N = int(input())
    boxes = list(map(int, input().split()))

    # 정렬 후 max, snd_max, min, snd_min 구하기



    new_boxes = sorting(boxes)
    counts = 1



    #
    # min = new_boxes[0]
    # max = new_boxes[-1]
    # i_min, i_max = -1, 0

    #             666
    #
    #       444444
    #
    #   2222
    # 11                 여기서 (6 - 4) 가 밑에 max-minus 값



    while counts <= N :




        # for i in range(new_boxes):  # 최소값 바로 다음 인덱스 찾기
        #     if new_boxes[i] > min:
        #         i_min = i
        #         break
        # for i in range(len(new_boxes) - 1, -1, -1):  # 최대값 바로 다음 인덱스 찾기
        #     if new_boxes[i] < max:
        #         i_max = i
        #         break
        # max_minus = new_boxes[-1] - new_boxes[i_max] # 새로 값 부여해서 빼주기 전까지 젤 큰애한테서 빼줘도 될 값
        # min_minus = new_boxes[i_min] - new_boxes[0]
        # while :
        #     i_max += 1
        #     i_min -= 1
        #     counts = 0
        #     while counts < max_minus :
        #         counts += 1
        #         new_boxes[i_max] -= 1
        #         new_boxes[i_min] += 1




        new_boxes[-1] -= 1
        new_boxes[0] += 1
        new_boxes = sorting(new_boxes)
        diff = new_boxes[-1] - new_boxes[0]
        counts += 1
        if diff <= 0:
            break
    print(f'#{tc+1} {diff}')





#1 13
#2 32
...



#홍성목