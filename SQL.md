# SQL

#### 분류

##### DDL(데이터 정의 언어)

- CREAT
- DROP
- ALTER

##### DML(데이터 조작 언어)

- INSER
- SELECT
- UPDATE
- DELETE

##### DCL(데이터 제어 언어)

db 사용자 권한 제어

- GRANT
- REVOKE
- COMMIT
- ROLLBACK



#### 데이터베이스 생성하기

visual studio code에서 아래를 입력하세요. 대충 맞을꺼야

```bash
$ sqlite3 db.sqlite3
```

앞에 친건..원래 명령어 이름 다른데 vim(메모장) 들어가서 저걸로 바꾼거임. 꼬우면 니도 찾아서 바꾸든가

뒤에는 `장고에서 migrate 했을 때 만들어진 데이터베이스 파일명`.squlite3

```sqlite
sqlite > .tables
```

`.`는 sqlite 프로그램의 기능을 실행하는 것

이렇게 함 table에 뭐 있는지 확인해주시고

```sqlite
sqlite > .mode csv
sqlite > .import users.csv users_user
```

엑셀파일같이 생긴 데이터베이스 파일이 있음

.csv확장자 파일임 ㅇㅋ? import 뒤에는 그거 입력하는거고

그 뒤에는 그 파일을 넣을 데이터베이스 테이블 이름인듯...



참고

```sqlite
sqlite > .headers on
sqlite > .mode column
```

테이블 그... 칼럼도 위에 표시해주는거랑

칼럼에 맞게 딱딱 표처럼 만들어주는애임 근데 못생기게 만들어줘서 별로 의미 없는것같기도...^^;



코드 작성후에 작성한 부분 블락처리하고 우클릭해서 run selected query한 담에 새로고침 하면 데이터베이스에 적용되어있음



## 테이블 생성 삭제 + ALTER

````sql
CREAT TABLE `테이블 이름`(
    # 스키마 입력
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
    age INT 
);
# 보시다시피 not null을 지정해줄 수도 있고
# `컬럼 이름` `value type` ` null 여부` 로 적어줌
# 근데 ID 저렇게 명시적으로 지정하지 마셈. 걍빼버리라고. 안그러면 값 넣을 때마다 쟤도 명시해야하거든. 무슨뜻인지는 밑에 crud에서!
````

```sql
DROP TABLE `테이블 이름`;
# 이라고 하면 삭제 ㅇㅇ
```



### ALTER

- table 이름 변경

```sql
ALTER TABLE 테이블원래이름 RENAME TO 새이름;
```

- 새로운 column 추가

```sql
ALTER TABLE 테이블이름 ADD COLUMN 컬럼이름 데이터타입 등등;
# NOT NULL 설정하려면 DEFAULT 디폴트값; 도 같이 뒤에 지정해줘야함!
```



- column 이름 수정

```sql
ALTER TABLE 테이블이름
RENAME COLUMN 예전컬럼이름 TO 컬럼새이름;
```



## 기본 CRUD 로직

### 삽입

```sql
INSERT INTO 테이블이름 (컬럼1, 컬럼2, ...) VALUES (값1, 값2, ....);
```

컬럼 값들 다 순서에 맞게 입력할꺼면 (컬럼1, ...) 부분은 없어도 됨

근데 ID를 명시적으로 스키마에 표시해버리면 얘도 명시해야하는 값으로 인식 즉 (ID값, 값1, 값2, ...) 이렇게 적을꺼아니면 무조건 (컬럼1, 컬럼2, ...) VALUES (값1, 값2, ...) 이렇게 해야한다는 의미ㅠ



### 조회

##### 모든 레코드 조회

```sql
sqlite > SELECT * FROM users_user
```



##### SELECT와 함꼐 사용하는 clause들

- LIMIT
  - 행수 제한
  - OFFSET을 쓰면 특정 행부터 조회
- WHERE
  - 조건 지정 후 행 읽어들이기
- SELECT DISTINCT
  - 중복 행 제거
  - SELECT 키워드 바로 뒤에 작성!



##### 특정 컬럼만 조회 + limit 쓰기

```sql
SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 LIMIT 숫자 OFFSET 숫자-1;
SELECT rowid, name FROM users_user LIMIT 5 OFFSET 4;
```

##### WHERE

```sql
SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 WHERE 조건; 

SELECT rowid, name, address FROM 테이블이름 WHERE address='서울';

SELECT rowid, name, age FROM 테이블이름 WHERE age >= 30 AND last_name = '김';
```

##### DISTINCT

```sql
SELECT DISTINCT 컬럼 FROM 테이블이름;
SELECT DISTINCT age FROM users_user;

# 결과값
age
---------
30
26
29
28
```



##### 총...숫자 세기

```
SELECT COUNT(*) FROM users_user
```





### 삭제

```
DELETE FROM 테이블이름 WHERE 조건;
# 조건에는 보통 음... 유일한 값인 rowid을 넣어줘서 삭제함
```



### 수정

```
UPDATE 테이블이름 SET 컬럼1=값1, 컬럼2=값2, ... WHERE 조건;
```



### Aggregate function(집계 함수)

#수학 #계산 #숫자 #세기 #최대값 #최소값 #합 #평균 

SELECT구문에서 사용

- COUNT
- AVG
- MAX
- MIN
- SUM

```sql
SELECT COUNT(컬럼) FROM 테이블이름 WHERE ~;
# 다른것들도 다 똑같음
# 카운트에서 컬럼은 음... 아마 중복빼고 조회하는거인듯
SELECT COUNT(*) ~
# 이러면 전체 조회
SELECT AVG(age) FROM users_user WHERE age>=30;
# 나이 30 이상 유저의 평균 나이 계산
```

```
SELECT first_name, MAX(balance) FROM users;
```



### LIKE operator

#패턴 #시작 #끝 #검색 #키워드

- % : 0개 이상의 문자

- _ : 임의의 단일 문자
- wildcard character과 비교(*, ?)

```sql
SELECT * FROM 테이블 WHERE 컬럼 LIKE 2_%_%
# `컬럼`안의 값 중 2로 시작하고 적어도 3자리인 값을 전부 조회
# 2__%로 해도 됨
```



### ORDER BY

```sql
SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;
# 나이, 성 오름차순으로 정렬한 후 10개만 뽑아
SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;
# 잔액순으로 정렬해서 10명 이름 뽑아
```



### GROUP BY

```sql
SELECT 컬럼1, aggregate_function(컬럼2) FROM 테이블 GROUP BY 컬럼1, 컬럼2;
SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;
# users를 성씨별로 묶어서 성씨랑 각 성씨에 속한 사람 수 출력
# 근데 카운트 컬럼명을 name_count로 변경
```



