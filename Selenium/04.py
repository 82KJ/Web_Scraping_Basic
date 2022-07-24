from selenium import webdriver
import time
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 만약 headless chrome으로 동작을 원하면 다음 코드를 추가한다
options.headless = True
options.add_argument('window-size=1920x1080')
#options.add_argument('user-agent=') 를 붙어주어야지 headless chrome의 차단을 막을 수 있다
############################################################

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = 'https://play.google.com/store/movies/collection/cluster?clp=4g46ChMKDUZNNFpMbmJ6Wnl3LlAQBhgEEg0vZy8xMWptcXAzbV83GgovbS8wMmtkdjVsKgbslaHshZhABQ%3D%3D:S:ANO1ljKZbdA&gsr=Cj3iDjoKEwoNRk00WkxuYnpaeXcuUBAGGAQSDS9nLzExam1xcDNtXzcaCi9tLzAya2R2NWwqBuyVoeyFmEAF:S:ANO1ljIQr4g'
browser.get(url)

interval = 2
prev_height = browser.execute_script('return document.body.scrollHeight') # 현재 높이

while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2) # 2초

    cur_height = browser.execute_script('return document.body.scrollHeight') # 현재 높이

    if prev_height == cur_height : break

    prev_height = cur_height


soup = BeautifulSoup(browser.page_source, 'lxml')

movies = soup.find_all('div', attrs={'class' : 'ULeU3b'})

for movie in movies:
    title = movie.find('div', attrs={'class' : 'Epkrse'}).get_text()

    # 할인 전 가격
    original_price = movie.find('span', attrs={'class' : 'SUZt4c P8AFK'})
    if original_price:
        original_price = original_price.get_text()
    else:
        #print(title, " <할인되지 않은 영화 제외>")
        continue

    new_price = movie.find('span', attrs={'class' : 'VfPpfd VixbEe'}).get_text()
    link = 'https://play.google.com'+movie.find('a', attrs={'class' : 'Si6A0c ZD8Cqc'})['href']
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {new_price}")
    print(f"링크 : {link}")
    print('==================================\n')