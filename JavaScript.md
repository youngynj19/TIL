# JavaScript

#### Spread operator

- ...array = 파이썬에서 *array랑 같은 느낌

### String

#### method

- split

```js
const str = 'a cup'
const str1 = str.split('') //['a', ' ', 'c', ...]
const str2 = str.split(' ') //['a', 'cup']
```

- trim

```javascript
const str = '     hello     '
const str1 = str.trim() // 'hello'
str.trimStart()
str.trimEnd()
```



### Arrays

#### methods

- .reverse() : 배열을 반대로 정렬
- push()/pop()/unshift()/shift() : 맨뒤/맨앞 - 넣거나/빼거나
- .includes() : 특정 값 존재 판별 후 T/F 반환
- .indexOf() : 해당 값 없으면 -1 반환
- join

```javascript
const numbers = [1, 2, 3, 4, 5]
let result
result = numbers.join() // 1,2,3,4,5
result = numbers.join('') // 12345
result = numbers.join(' ') // 1 2 3 4 5
result = numbers.join('-') // 1-2-3-4-5
```



#### Array Helper Methods

호출 시 인자로 `callback 함수`를 받음

- forEach : 반환값(retrun) 없음

```javascript
array.forEach((element, index, array) => {
	// do something
})
```

- map : 각 요소에 콜백함수 실행한 결과를 요소로하는 새로운 배열 반환

```
const numbers = [1, 2, 3, 4, 5]
```

