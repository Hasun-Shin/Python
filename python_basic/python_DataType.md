# 파이썬 자료형

리스트 : 수정가능

튜플 : 수정 불가. 괄호 안에 삽입은 가능하나 수정 불가능

set : 중괄호 안에 숫자. 집합. 중복데이터를 허용하지 않음. 순서가 없음 .



- **Formatting** 

문장이 나옴. 부분부분에 숫자나 문자열을 표현할건지 % 를 이용해서 위치 선정

%d : 정수

예 ; 'Pyton vesion %d' %1

'%s version %d' %(python, 3)

**{index}**

**{name}**

'{0},{1}'.format('score',70)

'score 70'

**중괄호와 함수 이용 **

----------

**find ()**:특정 문자 위치

str.find(' ', 5) : 공백을 5번 위치부터 찾아라. 

**-join()** : 각 문자 사이에 문자 삽입

 **rstrip()** : 오른쪽 공백 삭제

 **lstrip()** : 왼족 공백 삭제

**split()** : 특정 문자열을 기준으로 전체 문자열을 **리스트**로 변경

예 : str.split('o') 

['Life is t', '', ' sh', 'rt, Y', 'u need Pyth', 'n']

split할때 쓰인 인자는 사라진다. 

----------

● List 요소 값 수정

 list[1] = list[1] * 2 [10, 4, 3, 4, 5]

- 튜플

  List 와의 차이점 

  - List : 요소 추가/수정/삭제 가능 (mutable)
  - Tuple : 요소 수정/삭제 불가 (immutable)

  

-------

**딕셔너리** 

중괄호, 소괄호 둘 다 사용 가능 

- Dictionary 요소 값 확인

 dict['b'] 대괄호 사용 ! 

- key는 변경 불가, 변경이 가능한 값은 key로 사용 불가

  > dict = { 'a' : 1, 1 : '가' } # O 
  >
  > dict = { (1, 2, 3) : 'tuple' } # O 
  >
  > dict = { [1, 2, 3] : 'list' } # X 
  >
  >  dict = { {1:'a'} : 'dict' } # X

-  keys() : key의 목록 확인

    dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 } 

  > >> dict.keys() dict_keys(['a', 'b', 'c', 'd', 'e']

- values() : value의 목록 확인 (≠ List)
- items() : key, value 목록 확인 (≠ List) 

튜플 형식의 목록이 만들어짐. 

----------

변수 

- 요소복사
- 참조 : 0x100
- 기본 : 100

- mutable : List,Dictionay,Set (깊은 복사)
  - 예를 들어, 리스트인 경우, list2 =list1 을 할 때, 값인 기본이 아니라, 참조(주소) 가 복사 되어서 list2를 변경하면 덩달아 list1도 변화한다. 
  - 그러므로, 얕은 복사를 (기본 값만 복사) 시키려면 list2 = list1[:] 이라고 해야한다. 
- immutable : Tuple, Number, String(얕은 복사)