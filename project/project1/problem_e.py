import json


def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.
    # max = 0 # 최대값 대입
    # comp = 0 # 이전 최대값과 비교할 값 대입
    # result = ''
    movies_Dec = [] # 12월 개봉 영화 리스트
    for movie in movies: # movies의 각 영화에 대해...
        for key in movie:
            if key == "id": # 해당 영화의 id에 해당하는 상세정보 파일 dict에 옮기기
                movie_jason = open(f'data/movies/{movie.get(key)}.json', encoding='UTF8')
                movie_dict = json.load(movie_jason) # 해당 영화의 id에 해당하는 상세정보 파일 dict에 옮김!
                for key_detail in movie_dict:
                    if key_detail == "release_date": # "key=release_date"에 대해
                        release_date = list(map(int, 
                                       movie_dict.get(key_detail).split('-'))) # [yyyy, mm, dd] 도출
                        if release_date[1] == 12: # 12월의 영화 리스트에 하나씩 추가
                            movies_Dec += [movie_dict.get("title")]
    return movies_Dec  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))