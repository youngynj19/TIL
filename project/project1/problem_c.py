import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.
    result = [] # 반환할 리스트
    showthx = {} # 반환할 리스트에 넣을 "영화 정보 딕셔너리"
    key_ls = ["id", 'title', 'poster_path', 
    'vote_average', 'overview', 'genre_ids'] # 필요한 key 집합
    for movie in movies:
        for i in movie:
            if i in key_ls: # movie의 key중 key_ls에 해당하는 값만 입력
                if i != "genre_ids": # genre_ids는 바꿔서 입력, 나머지는 그대로 입력
                    showthx = showthx | {i: movie[i]}
                else:
                    gen_names = [] # genre_names에 담을 이름 리스트
                    for j in genres: # genres.jason에 있는 dict들을 순회하면서...
                        for k in movie[i]: # "genres.jason의 id"와 "호출자 genres_ids에 있는 장르 넘버들" 비교
                            if j["id"] == k:
                                gen_names += [j["name"]] # gernre_names에 담을 이름 추가
                    showthx = showthx | {"genre_names": gen_names} # genre_names 입력
        result += [showthx] # 만들어진 dictionary 하나씩 반환 리스트에 추가

    return result
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))