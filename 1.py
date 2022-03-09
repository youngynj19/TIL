    result = {}
    for n in range(1, 3):
    
    
    
        query={
            'api_key': 'b9660b80b0f8d1b38113a8e59bb595ff',
            'region': 'KR',
            'page': n
        }
        # 위의 세 변수로 인기있는 영화들을 보여주는 웹페이지 입력받기

        r = requests.get(BASE_URL+path, params=query).json()
        result |= r['results']    
    
    
    
    
    # 해당 페이지에서 영화 정보만 반환
    pprint(result)
