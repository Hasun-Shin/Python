import requests
from bs4 import BeautifulSoup

url = "http://finance.naver.com/sise/"

# request = requests.get(url)
request = requests.get(url).text
#print(request)

soup = BeautifulSoup(request, 'html.parser') #html 형식을 parsing 하도록 명령함. 
#print(soup) -> html 문서 전체가 출력됨
kospi = soup.select_one("#KOSPI_now") #url 에서 원하는 정보 selector copy 함 -> 하나씩 뽑아서 출력해줘.
print(kospi.text) #텍스트만 출력하기. 