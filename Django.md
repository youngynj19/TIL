# Django

## introduction

Dynamic web page (동적 웹 페이지) <-> Static ~



#### framework

- 프로그래밍에서 특정 운영 체제를 위한 응용 프로그램 표준 구조를 구현하는 클래스와 라이브러리 모임

#### web framework

- 웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적



### MTV pattern(=MVC)

#### Model

- app의 데이터 구조 정의, 데이터베이스 기록 관리(추가, 수정, 삭제)

#### Template

- 파일 구조 or 레이아웃 정의
- 실제 내용 보여주는데 사용

#### View

- HTTP 요청 수신 + HTTP 응답 반환
- Model을 통해 요청 충족 필요한 데이터에 접근
- Template에게 응답의 서식 설정 맡김



## starting

```bash
$ python -m venv (name)
$ source (name)/Scripts/activate
$ pip list
$ pip istall django-3.2.12
$ django-admin startproject (name) .
$ python manage.py runserver
$ paython manage.py startapp (name)
```

앱 등록: settings.py의 INSTALLED_APPS에서 `'(name)',` 추가

- #### 생성 후 등록!



##### jango 사전 준비사항

##### vscode django extension 설치

원할한 코드 작성을 위해 django 확장 프로그램 설치를 권장합니다.

Django

Excel Viewr

vscode 내 확장프로그램에서 두 개 설치

------

##### django extension 설정

1. `ctrl(command) + shift + p` → `json`검색 → `Preferences: Open Settings (JSON)` 선택

2. 설정 코드 작성

   ```jsx
   // settings.json
   
   {
     ... 생략 ...,
   
     // Django
     **"files.associations": {
       "**/*.html": "html",
   	    "**/templates/**/*.html": "django-html",
       "**/templates/**/*": "django-txt",
       "**/requirements{/**,*}.{txt,in}": "pip-requirements"
     },
     "emmet.includeLanguages": {
       "django-html": "html"
     }**
   }
   ```



## 요청과 응답

urls.py에는 django.urls로부터 path랑 `include` 가져오셈

```
urlpattern = [
	~
	path('(name)/', include('(name).urls')),
]
```



## model

#### validator

​	자료 값에 limit을 정해줌

```python
title = models.CharField(max_length=100, validator=)
age = models.IntField(validator=)
```





## forms

#### 스타일 지정

1.  따로 따로 다 지정

```html
<div>
  {{ form.title.errors }}
  {{ form.title.label_tag }}
  {{ form.title }}
</div>
```



2. 부트스트랩 라이브러리

```
{% load bootstrap5 %} 하고 이것저것 하는거 있는데 강의 다시 보면서 정리하셈
```



#### 유효성 검사

view함수에서 실행

- forms.Form으로 작성시

```python
def create(request):
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data.get('title')
			# content도 똑같이
			article = Article.objects.create(title=title, content = content)
			return redirect(article)
```

- forms.ModelForm으로 작성 시 - cleaned_data 필요없고 걍 바로 만드셈



## 쿠키와 세션

#### http 특징

- 비연결지향
- 무상태 - 정보상태 유지X
- 그래서... 쿠키와 세션이 필요!

#### 쿠키

- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각(기록 정보 파일)
- 쿠키가 하는 일
  - 세션 만들기 - 정보상태 키값을 내컴퓨터에 저장해놓고 서버에 매번 보내주는거지 - 그럼 
  - 어쩌구저쩌구

### 세션 관리

- 4/11 웹엑스

### 로그인 & 로그아웃

## 데이터베이스 관계(1:N)

### 댓글

### 유저

