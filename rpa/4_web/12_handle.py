from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get(
    'https://www.w3schools.com/tags/att_input_type_radio.asp')
curr_handle = browser.current_window_handle
print(curr_handle)

browser.find_element_by_xpath('//*[@id="main"]/div[2]/a').click()

handles = browser.window_handles  # 모든핸들정보 가져오기.
for handle in handles:
    print(handle)
    browser.switch_to.window(handle)  # 핸들로 이동해서
    print(browser.title)  # 현재 브라우저의 제목
    print()

time.sleep(5)
browser.quit()
