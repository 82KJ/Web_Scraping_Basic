import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all('a', attrs={'class' : 'title'})
for cartoon in cartoons:
    print(cartoon.get_text())

# 가우스 전자 시즌3~4 크롤링
url = 'https://comic.naver.com/webtoon/list?titleId=675554'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# 가우스 전자 시즌3~4 첫 title, link 정보 출력
cartoons = soup.find_all('td', attrs={'class':'title'})
title = cartoons[0].a.get_text()
link = 'https://comic.naver.com' + cartoons[0].a['href']
print(link, title)

# 나머지 정보도 출력
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = 'https://comic.naver.com' + cartoon.a['href']
    print(link, title)

# 평점 정보 구하기 + 평균 구하기
total_rates = 0
cartoons = soup.find_all('div', attrs={'class':'rating_type'})
for cartoon in cartoons:
    rate = cartoon.find('strong').get_text()
    print(rate)
    total_rates += float(rate)
print('전체 점수 : ', total_rates)
print('평균 점수 : ', total_rates/len(cartoons))