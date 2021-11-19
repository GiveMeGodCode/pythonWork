import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()

browser.get('https://www.w3schools.com/html/')
browser.maximize_window()

time.sleep(5)

# 특정영역 스크롤
elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[62]')

# ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

xy = elem.location_once_scrolled_into_view  # elemeny 의 좌표 정보

print("type :", type(xy))
print("value :", xy)

elem.click()

time.sleep(10)
browser.quit()
