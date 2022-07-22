import re

# . --> 하나의 문자
# ^ --> 문자열의 시작
# $ --> 문자열의 끝 

p = re.compile("ca.e")

def print_match(m):
    if m:
        print(m.group()) # 일치하는 문자열 반환
        print(m.string) # 입력받은 문자열
        print(m.start()) # 일치하는 문자열의 시작 index
        print(m.end()) # 일치하는 문자열의 끝 index
        print(m.span()) # 일치하는 문자열의 시작, 끝 index
    else:
        print("매칭되지 않음")

m = p.match("case")
print_match(m) # case 출력

m = p.match("good care") # error
m = p.match("careless") # care출력 --> match는 주어진 문자열을 처음부터 비교하여 일치하는지 확인

# search는 주어진 문자열 중에 일치하는게 있는지 확인
m = p.search("good care") 
print_match(m) # care 출력

# findall은 일치하는 모든 것을 리스트 형태로 반환
lst = p.findall("good care cafe")
print(lst) # ['care', 'cafe']

# 더 공부하고 싶다면, w3school의 python RegEx 활용하기
