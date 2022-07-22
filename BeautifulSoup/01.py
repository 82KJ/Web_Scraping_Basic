import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 01. page 구조를 잘 알고 있을 때 사용
print(soup.title)
print(soup.title.get_text())
print(soup.a) # 첫번째 a 태그 정보만 가져옴
print(soup.a.attrs) # a 태그의 attribute 정보를 딕셔너리 형태로 반환
print(soup.a["href"]) # a 태그의 href attribute 정보를 반환

# 02. 잘 모른다? 그럼 분석해야지
print(soup.find("a", attrs={"class":"Nbtn_upload"}))  # class attribute를 만족하는 첫 a태그를 찾음
print(soup.find(attrs={"class":"Nbtn_upload"})) # 단, tag가 없어도 찾을 수 있다
rank1 = soup.find('li', attrs={"class":"rank01"})
print(rank1.a)