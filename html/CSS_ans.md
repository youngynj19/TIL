# CSS

#### 선택자 적용 우선순위

1. !important
2. 인라인 > id > class, 속성, psudo-class > 요소, pseudo-eldlment
3. CSS 파일 로딩 순서



#### 크기단위

디바이스 or 창 크기에 따라

```tex
vw, vh, vmin, vmax
```



#### 박스 사이즈 수정

```html
box-sizing: border-box
```



### 인라인 vs 딴거

```html
display: block
display: inline
display: inline-block
display: none
<!-- visibilty: hiden 과 구분 -->
```

- 인라인은 width, height, margin-top, margin-bottom 지정 불가
- 인라인 상하여백 line-height로 지정 가능



### position

```html
position: relattive; top: 100px; left: 100px
position: absolute;
position: fixed
position: sticky
```

- absolute는 static이 아닌 조상 요소 기준 이동



### flex

```html
flex-directioin: row-reverse or column-*
fles-wrap: nowrap or wrap or wrap-reverse
flex-flow: direction 다음에 wrap

justify-content / align-content
: flex-start / fles-end / center / space-between / space-around / space-evenly

align-items / align-self
: start / end / center / stretch / baseline

flex-grow / order
```

