import requests
from bs4 import BeautifulSoup

url = "http://www.naver.com"

req = requests.get(url).text
soup = BeautifulSoup(req,'html.parser') 
#파싱할 정보,
now = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k') #실시간 검색 정보가 저장되어 있는 slector 
for i in now :
    print(i.text)

