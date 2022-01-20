def get_middle_char (char):
    result = '' # 결과값 변수
    midd = 0 # char의 중간 길이
    counts = 0 # char의 길이
    
    for c in char: # 를 측정
        counts += 1

    i = 0 # indicating when c gets to the middle
    for c in char:
        i += 1
        if i == int(counts / 2): # i reached the middle
            if counts % 2: # if counts is odd number get the character and finish the rotation
                result = c
                break
            else: # if counts is even number, get the character and do one more rotation
                result = c
        elif i == int(counts / 2) + 1: # second character for the case of even number
            result += c
            break

    return result

print(get_middle_char('wheat'))

# midd = counts // 2
# if length % 2 == 0:
#   result = char[midd-1:midd+1] 문자열도 컨테이너이고... 슬라이싱이 있따는거....
# result는 걍 조건문 안에서 선언하셈
# 그리고 midd는 가독성을 위해 설정하는걸 추천드림ㅋ