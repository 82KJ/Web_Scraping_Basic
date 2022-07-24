from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = 'https://flight.naver.com/'
browser.get(url)

# 도착지 선정
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[1]/div/input').send_keys('제주')
time.sleep(1)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/div/a').click()

# 출발, 도착 일자 선정
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[5]/button').click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[6]/button').click()

# 항공권 검색 클릭
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click()

# 이후, 최대 10초까지 대기하면서, 해당 XPATH를 찾으면 ELEM을 받아옴
try:
    elem = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[2]')))
    print(elem.text)
finally:
    browser.quit()
