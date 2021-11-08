import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get(
    'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult')

browser.maximize_window()

elem = browser.find_element_by_xpath('//*[@id="html"]')

# 선택이 안되어 있으면 선택하기
if elem.is_selected() == False:
    print("선택안되어있으므로 선택하기")
    elem.click()
else:
    print("선택이 되어있어서 아무것도 하지 않음")

# 선택이 안되어 있으면 선택하기
if elem.is_selected() == False:
    print("선택안되어있으므로 선택하기")
    elem.click()
else:
    print("선택이 되어있어서 아무것도 하지 않음")


time.sleep(5)  # 5초 대기
