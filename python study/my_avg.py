def my_avg(*args):
    counts = 0 # 갯수 반환
    result = 0 # 총합 반환
    for i in args:
        counts += 1
        result += i
    return result / counts

print(my_avg(77, 83, 95, 80, 70))

# *얘가 언패킹 연산자도 된다고 했찌? 언제?

print(*[[1,2], [3,4]])
이럴 때 겉 껍질 한 겹 벗겨줌