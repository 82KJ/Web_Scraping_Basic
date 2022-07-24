import requests
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

def scrape_weather():
    print('오늘의 서울 날씨')
    soup = create_soup('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8')

    summary = soup.find('p', attrs = {'class' : 'summary'}).get_text()
    cur_temp = soup.find('div', attrs={'class' : 'temperature_text'}).get_text().strip()[5:-1]
    min_temp = soup.find('span', attrs={'class' : 'lowest'}).get_text()[4:-1]
    max_temp = soup.find('span', attrs={'class' : 'highest'}).get_text()[4:-1]
    weather = soup.find('div', attrs={'class' : 'cell_weather'}).find_all('span', attrs={'class' : 'rainfall'})
    am_rainfall = weather[0].get_text()
    pm_rainfall = weather[1].get_text()

    print(summary)
    print('현재 {}° (최저 {}° / 최고 {}°)'.format(cur_temp, min_temp, max_temp))
    print('오전 강수확률 {} / 오후 강수확률 {}'.format(am_rainfall, pm_rainfall))

def scrape_headline():
    print('\n오늘의 정치 헤드라인 뉴스')
    soup = create_soup('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100')

    # with open('test.html', 'w', encoding='utf-8') as f:
    #     f.write(soup.prettify())

    headlines = soup.find_all('div', attrs = {'class' : 'cluster_text'})
    for i in range(3):
        headline = headlines[i].a.get_text()
        url = headlines[i].a['href']
        print(f'{i+1}. {headline} [주소 : {url}]')

if __name__ == '__main__':
    scrape_weather()
    scrape_headline()