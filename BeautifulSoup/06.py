import csv
import requests
from bs4 import BeautifulSoup

filename = '시가총액1-200.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline= '')
writer = csv.writer(f)
writer.writerow('N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실'.split())

for page in range(1,5):
    url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={}'.format(page)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    tr = soup.find('tbody').find_all('tr')
    for row in tr:
        columns = row.find_all('td')

        # blank skip
        if len(columns) <= 1 :
            continue

        data = [column.get_text().strip() for column in columns]
        writer.writerow(data)