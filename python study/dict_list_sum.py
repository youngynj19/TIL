def dict_list_sum(kargs):
    counts = 0
    for dic in kargs:
        for key in dic:
            if key == 'age':
                # print(dic[key])
                counts += dic[key]
    # print(counts)
    return counts
    
dict_list_sum([{'name': 'kim', 'age': 12}, 
                {'name': 'lee', 'age': 4}])
# 누가 봐도 딕셔너리{}에는 이름이랑 나이밖에 없잖아
# 걍 리스트[i]['age'] 하면 되겠구나 생각을 했어야함