import json


def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.
    max = 0 # 최대값 대입
    comp = 0 # 이전 최대값과 비교할 값 대입
    result = ''
    for movie in movies: # movies의 각 영화에 대해...
        for key in movie:
            if key == "id": # 해당 영화의 id에 해당하는 상세정보 파일 dict에 옮기기
                movie_jason = open(f'data/movies/{movie.get(key)}.json', encoding='UTF8')
                movie_dict = json.load(movie_jason) # 해당 영화의 id에 해당하는 상세정보 파일 dict에 옮김!
                for key_detail in movie_dict:
                    if key_detail == "revenue": # "key=revene"에 대해
                        comp = movie_dict.get("revenue") # 해당 수익 비교용 변수에 넣어놓고
                        if comp > max: # 비교값이 max보다 크다면 max 업뎃 + 해당 영화이름 저장
                            max = comp # 그런데 첫 번째 비교시에는 max=0 => 첫 번째 영화이름, 수익 일단 저장됨
                            result = movie_dict.get("title")
    return result

 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))