# REST API

#### URL / URN / URI



### URI의 구조

#### Port



#### Path

웹 서버상 리소스 경로



#### Query

- Query String Parameters
- /?=싸피&~~~



#### Fragment

- #~~~
- 북마크 같은 거

페이지에서 스크롤 쭉 내리다가 아! 여기! 하는 그 부분도 북마크 해줘서 그 주소를 친구들이랑 공유할 수 있는거지

- 서버에 보내지지는 않고 브라우저한테 보내줘서 브라우저가 처리함.



### API

##### 애플리케이션과 프로그래밍으로 소통하는 방법 중 하나

CLI(글로 쭉 쓰는거) 도 있고 GUI(그래픽)도 있고

그리고 API도 있고!

##### 웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세

- 현재 웹 개발은 모든 것을 직접 개발하기보다 여러 Open API를 활용



### REST

##### REpresentational State Treanfer

##### API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론 중 하나



##### 자원과 주소의 지정 방법

- 자원(정보) : URI
- 행위 : HTTP Method
  - GET
  - POST
  - PUT
  - DELETE
- 표현 (응답)(자원과 행위를 통해 궁극적으로 표현되는추상화된 결과물??)
  - JSON으로 표현
  - 그러나 우리는 지금껏 HTML으로 했었지



### JSON

##### JavaScript Object Notation

- JAvaScript의 표기법을 따른 "단순 문자열"

- 근데 키-밸류 형태로 이루어져있어서 여러 언어로 변환이 쉬움
  - 파이썬에서는 딕셔너리 형태로ㅇㅇ