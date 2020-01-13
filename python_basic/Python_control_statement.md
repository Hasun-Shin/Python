## 복습

- 자료형
  - List : 수정가능
  -  Tuple : 수정 불가
  - Set : 집합. dic과 달리 key 가 없음. 중복 요소를 허락하지 않음. 



## 제어문

- 파이썬 의 for 

  - 50에서 1000까지 반복해 X.
  - for each 의 개념만 있음. 
  - 이미 1 ~ 10 까지 요소를 갖고 있고, 하나씩 요소를 뽑아내서 요소가 남아있지 않을 때 까지 사용한다. 

- 논리 연산자 사용

  - if native == '금수저' **or** money >= 10000:
  - If age >= 20 **and** hasIDCard:

- 조건부 표현식

  - print('PASS') if score >= 60 else print('FAIL')

  - msg = 'PASS' if score >= 60 else 'FAIL' 

    print(msg)

- While

- for-

  - List Comprehension

    ```python
    a = [1, 2, 3, 4]
    result = []
    for n in a:
     result += [n * 3] # result.append(n * 3)
    print(result)
    ```

    

    ```python
    a = [1, 2, 3, 4]
    result = [n * 3 for n in a]
    print(result)
    ```

    ```python
    a = [1, 2, 3, 4]
    result = [n * 3 for n in a if n % 2 == 0]
    print(result)
    ```

    