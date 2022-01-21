import json
from pprint import pprint


def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다.

    showthx = {} # 반환할 딕셔너리
    key_ls = ["id", 'title', 'poster_path', 
    'vote_average', 'overview', 'genre_ids'] # 필요한 key 집합
    
    for i in movie:
        if i in key_ls: # movie의 key중 key_ls에 해당하는 값만 입력     
            showthx = showthx | {i: movie.get(i)}    
    return showthx


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))