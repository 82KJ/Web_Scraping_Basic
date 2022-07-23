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

# page를 1부터 6으로 순환하면서 진행
for i in range(1,6):
    print('페이지',i)
    url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor='.format(i)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    items = soup.find_all('li', attrs={'class':re.compile("^search-product")})

    # 제품명, 가격, 평점, 평점 수 출력
    for item in items:
        name = item.find('div', attrs={'class' : 'name'}).get_text()
        price = item.find('strong', attrs={'class' : 'price-value'}).get_text()
        rate = item.find('em', attrs={'class' : 'rating'})
        rate_cnt = item.find('span', attrs={'class' : 'rating-total-count'})

        if rate:
            rate = rate.get_text()
        else:
            #print('평점 없는 상품 제외')
            continue

        if rate_cnt:
            rate_cnt = rate_cnt.get_text()
        else:
            #print('평점 수 없는 상품 제외')
            continue

        # 삼성 제품 제외
        if '삼성' in name:
            #print('삼성 상품 제외합니다')
            continue

        # 리뷰가 100개 이상, 평점 4.5이상만 조회
        rate_cnt = rate_cnt[1:-1]
        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            link = item.find('a', attrs={'class' : 'search-product-link'})["href"]
            print(f'제품명 : {name.strip()}')
            print(f'가격 : {price}')
            print(f'평점 : {rate}점 ({rate_cnt}개)')
            print('바로가기 : {}'.format('https://www.coupang.com' + link))
            print('======================================')
        else:
            #print('리뷰가 100건보다 적거나 평점이 4.5 미만입니다')
            continue

    