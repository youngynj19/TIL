# 첫 번째 프로젝트

## - 커뮤니티 서비스 개발을 위한 데이터 수집

### 목표

- **전체 데이터 중 필요한 데이터를 추출**



A. 제공되는 영화 데이터의 주요내용 수집 

- 영화데이터에서 서비스 구성에 필요한 정보만 뽑는 함수 구현



B. 제공되는 영화 데이터의 주요내용 수정 

- 현제 딕셔너리에서 genre_ids를 다른 딕셔너리에 있는 genre_names값으로 치환하는 함수 구현



C. 커뮤니티 서비스에서 제공되는 영화 목록 정리

- 다중 데이터 분석 및 수정 

- TMDB기준 평점이 높은 20개의 영화에 대해 A와 동일한 함수 구현



D. 가장 높은 수익을 낸 영화를 출력(메인 페이지 기본정보)

- 알고리즘을 통한 데이터 출력
- 세부적인 영화 정보 파일을 열어
- 모든 영화 중 가장 높은 수익을 낸 영화를 출력하는 알고리즘 작성



E. 12월에 개봉 한 영화들의 제목 리스트를 출력(커뮤니티 서비스에서 추천기능의 정보)

- 알고리즘을 통한 데이터 출력
- 세부적인 영화 정보 파일을 열어
- 12월에 개봉 한 영화들의 제목 리스트를 출력하는 알고리즘을 작성



### 에러 - 어떻게 해결

딕셔너리를 어떻게 새로 구성하지? 어떻게 합치지?

- 합집합 연산자^^ 자바 배울 때 잘 안썼어서 경시하고 있었는데... 배운 **모든** 내용 꼼꼼히 확인할 것!!!

코드 복붙할 때 코드 처음부터 끝까지 변수 함 살펴보고 돌리셈제발



### 추가로 배운 사항

딕셔너리를 그냥 +=로 리스트에 쑤셔넣었다가는 key밖에 안남는 불상사가 일어납니다.

- [딕셔너리]로 리스트로 만든담에 +=하셈

리스트 += 딕셔너리.get("key") 하면 하나씩 끊어서 입력됨 ... [딕셔너리.get("key")] 해줘야함

제이슨 파일 여는 법

```python
	movies_json = open('data/movies.json', encoding='UTF8')
	movies_list = json.load(movies_json)
```



** for문에 서 돌린 변수도 대충 i로 짓지말고 예쁘게 지어주셈