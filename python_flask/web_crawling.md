# 웹 크롤링을 위한 가상환경 설치

1. git bash 에서 pip list 설치 

(commit -m은 메세지, python -m 은 module)



2. $ python -m venv venv 가상환경 설치  세팅.



3.  source venv/Scripts/activate



4. 삭제하려면 deactivate

   가상환경 폴더 삭제 : rm -rf venv/



5. pip freeze 

6. pip freeze > requirements.txt . 텍스트 파일에 저장하여 사용함. 



7. pip install -r requirements.txt (모듈 없는 상태에서는 아무것도 없는 것이 맞음)



8. 가상환경 다시 켠 상태에서 pip install requests 설치하기. 
9. pip install beautifulsoup4 설치하기.





---------

# 웹 크롤링 

## 예제1. naver 주식에서 kospi 정보 받아오기

```python
import requests
from bs4 import BeautifulSoup # -> 다른 방식으로 import 하기 

url = "http://finance.naver.com/sise/"

# print(request)  : responce 200 -> 잘 출력 되었다
# request = requests.get(url) : html 형식으로 나옴.
request = requests.get(url).text


soup = BeautifulSoup(request, 'html.parser') 
# url 에서 원하는 정보 selector copy 함 
#html 형식을 parsing 하도록 명령함. 

print(soup)
```





## 예제 2. 미국 환율정보 알아보기 

```python
import requests
from bs4 import BeautifulSoup # 파이썬이 읽을 수 있게 바꿔줌

url = "http://finance.naver.com/marketindex"
req = requests.get(url).text
soup = BeautifulSoup(req,'html.parser') 
#파싱할 정보,
exchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value') #미국 달러 정보가 저장되어 있는 slector 
print(exchange.text)
```



## 예제 3. 네이버 실시간검색어 가져오기

```python
import requests
from bs4 import BeautifulSoup

url = "http://www.naver.com"

req = requests.get(url).text
soup = BeautifulSoup(req,'html.parser') 
#파싱할 정보,
now = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k') #실시간 검색 정보가 저장되어 있는 slector 
for i in now :
    print(i.text)
```





