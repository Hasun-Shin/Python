import requests
from bs4 import BeautifulSoup # 파이썬이 읽을 수 있게 바꿔줌

url = "http://finance.naver.com/marketindex"
req = requests.get(url).text
soup = BeautifulSoup(req,'html.parser') 
#파싱할 정보,
exchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value') #미국 달러 정보가 저장되어 있는 slector 
print(exchange.text)



