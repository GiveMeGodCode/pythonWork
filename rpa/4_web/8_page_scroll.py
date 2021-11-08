import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.maximize_window()

browser.get(
    'https://shopping.naver.com/home/p/index.naver')
# 무선마우스 입력
elem = browser.find_element_by_xpath(
    '//*[@id="autocompleteWrapper"]/input[1]')

elem.send_keys('무선마우스')
time.sleep(1)
elem.send_keys(Keys.ENTER)
# browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]').click()
time.sleep(1)
# browser.execute_script('window.scrollTo(0,1080)')  # 스크롤하기
# browser.execute_script('window.scrollTo(0,2080)')  # 스크롤하기

# 가장 아래로 Scroll
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')


interval = 2  # 2초에 한번 스크롤을 해보자.

# 현재높이 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

# 반복수행
while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    time.sleep(interval)
    current_height = browser.execute_script(
        'return document.body.scrollHeight')

    if prev_height == current_height:
        break
    else:
        prev_height = current_height

browser.execute_script('window.scrollTo(0,0)')  # 스크롤하기


time.sleep(5)
