import requests
from bs4 import BeautifulSoup

def scrape_weather():
    print('오늘의 서울 날씨')
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8'
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

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



if __name__ == '__main__':
    scrape_weather()