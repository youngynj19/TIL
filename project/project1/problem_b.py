import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    showthx = {} # 반환할 딕셔너리
    key_ls = ["id", 'title', 'poster_path', 
    'vote_average', 'overview', 'genre_ids'] # 필요한 key 집합
    
    for i in movie:
        if i in key_ls: # movie의 key중 key_ls에 해당하는 값만 입력
            if i != "genre_ids": # genre_ids는 바꿔서 입력, 나머지는 그대로 입력
                showthx = showthx | {i: movie.get(i)}
            else:
                gen_names = [] # genre_names에 담을 이름 리스트
                for j in genres: # genres.jason에 있는 dict들을 순회하면서...
                    for k in movie.get(i): # "genres.jason의 id"와 "호출자 genres_ids에 있는 장르 넘버들" 비교
                        if j.get("id") == k:
                            gen_names += [j.get("name")] # gernre_names에 담을 이름 추가
                showthx = showthx | {"genre_names": gen_names} # genre_names 입력
    return showthx
       

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))