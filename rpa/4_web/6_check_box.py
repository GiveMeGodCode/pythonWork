
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

browser.get(
    'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')

browser.switch_to.frame('iframeResult')


elem1 = browser.find_element_by_xpath('//*[@id="vehicle1"]')
elem2 = browser.find_element_by_xpath('//*[@id="vehicle2"]')
elem3 = browser.find_element_by_xpath('//*[@id="vehicle3"]')

# 선택이 안되어 있으면 선택하기
if elem1.is_selected() == False:
    print("선택안되어있으므로 선택하기")
    elem1.click()
else:
    print("선택이 되어있어서 아무것도 하지 않음")

# 선택이 안되어 있으면 선택하기
if elem2.is_selected() == False:
    print("선택안되어있으므로 선택하기")
    elem2.click()
else:
    print("선택이 되어있어서 아무것도 하지 않음")

# 선택이 안되어 있으면 선택하기
if elem3.is_selected() == False:
    print("선택안되어있으므로 선택하기")
    elem3.click()
else:
    print("선택이 되어있어서 아무것도 하지 않음")

time.sleep(5)  # 5초 대기
