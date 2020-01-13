## 함수

- 입력되는 값의 개수에 따라 동적으로 처리 

  - 입력값을 모두 더하는 함수 (1, 2, 3 이면 6, 1, 2, 3, 4, 5 이면 15)

    ```python
     total = 0
     for n in args:
     total += n
     return total
    num = total(1, 2, 3)
    print(num)
    num = total(1, 2, 3, 4, 5)
    print(num)
    ```

- lamda

  - 일반적 함수

    ```python
    def plus(a, b):
     return a + b
    result = plus(10, 20)
    print(result)
    
    ```

    

  - 람다식 함수 :  lambda 인자1, 인자2, … , 인자n **:  표현식**

    ```python 
    plus = lambda a, b: a + b
    result = plus(10, 20)
    print(result)
    ```

    

람다 형식

list  comprehension 형식

람다 + list comprehension 합친 형식

