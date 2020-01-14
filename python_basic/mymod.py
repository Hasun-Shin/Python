def myfunc(a,b):
    return a + b



print('='*20)
print(__name__)


if __name__ == '__main__':
    myfunc(3, 5)

    ## if 문은 모듈 개발자만 사용할 수 있고, 다른 사람이 이 모듈 파일을 쓸때는 if문 아래 구문은 실행되지 않음. 개발자가 이렇게 테스트했구나 ~ 라고 알 수 있음. 