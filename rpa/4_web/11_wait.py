from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%ED%95%AD%EA%B3%B5%EA%B6%8C')
browser.maximize_window()
time.sleep(2)

browser.find_element_by_link_text('가는날 선택').click()
browser.find_elements_by_link_text('29')[0].click()
time.sleep(2)
browser.find_elements_by_link_text('5')[1].click()
time.sleep(5)

time.sleep(5)
browser.quit()
