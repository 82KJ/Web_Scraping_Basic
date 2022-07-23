import requests
from bs4 import BeautifulSoup
import re

headers = { 
    "accept-language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "accept-encoding":"gzip, deflate, br",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-mode":"document","sec-fetch-mode":"navigate",
    "sec-fetch-site":"none","sec-fetch-user":"?1","upgrade-insecure-requests":"1",
    'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

# 쿠팡 노트북 사이트 크롤링
url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=3&rocketAll=false&searchIndexingToken=1=6&backgroundColor='
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

# 첫 아이템 목록의 이름 출력
items = soup.find_all('li', attrs={'class':re.compile("^search-product")})
print(items[0].find('div', attrs={'class':'name'}))

