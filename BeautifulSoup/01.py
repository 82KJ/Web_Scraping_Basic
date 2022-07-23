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

# 02. find를 통한, 특정 태그, attribute 찾기
print(soup.find("a", attrs={"class":"Nbtn_upload"}))  # class attribute를 만족하는 첫 a태그를 찾음
print(soup.find(attrs={"class":"Nbtn_upload"})) # 단, tag가 없어도 찾을 수 있다

# 03. 형제, 부모 태그
rank1 = soup.find('li', attrs={"class":"rank01"})
print(rank1.a.get_text())
rank2 = rank1.next_sibling.next_sibling # 두번한 이유는 개행문자 제거를 위해
print(rank2.a.get_text())
rank1 = rank2.previous_sibling.previous_sibling
print(rank1.a.get_text())
print(rank1.parent) # rank1의 부모 태그

rank1 = rank1.find_next_sibling('li') # next_sibling의 횟수를 모를 때는 다음과 같이 태그를 지정해준다
print(rank1.a.get_text())

all_rank = rank1.find_next_siblings('li') # 모든 형제를 가져올 수도 있다 --> 배열의 형태
print(all_rank[1].a.get_text())

# 04. 특정 텍스트 기준 찾기
webtoon = soup.find('a', text ='조조코믹스-안 하던 짓 5화 : 일시정지')
print(webtoon.get_text())