from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
browser.get('http://naver.com')

# 1. 로그인 버튼 클릭
elem = browser.find_element_by_class_name('link_login')
elem.click()

# 2. id, pw 입력
browser.find_element_by_id('id').send_keys('naver_id')
browser.find_element_by_id('pw').send_keys('naver_pw')

# 3. 로그인 버튼 클릭
browser.find_element_by_id('log.login').click()
time.sleep(1)

# 4. id 새로 입력
browser.find_element_by_id('id').clear()
browser.find_element_by_id('id').send_keys('my_id')

# 5. html 정보 출력
print(browser.page_source)

browser.quit()
