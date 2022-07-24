from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
browser.get('http://naver.com')

# login 버튼 클릭
elem = browser.find_element_by_class_name('link_login')
elem.click()

browser.back()

# 검색창에 입력하기
elem = browser.find_element_by_id('query')
from selenium.webdriver.common.keys import Keys
elem.send_keys('김관중')
elem.send_keys(Keys.ENTER)

# 다음으로 이동 후 검색창에 입력하기
browser.get('http://daum.net')
elem = browser.find_element_by_name('q')
elem.send_keys('김관중')

# 다만, 이번에는 xpath를 이용해서 click을 한다
elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[3]')
elem.click()

browser.quit()