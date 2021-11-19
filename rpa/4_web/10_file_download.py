import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option(
    'prefs', {'download.default_directory': r'C:\workSpace\PYTHON_WORKSPACE'})

browser = webdriver.Chrome(options=chrome_options)

browser.get(
    'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')
browser.maximize_window()
browser.switch_to.frame('iframeResult')

elem = browser.find_element_by_xpath('/html/body/p[2]/a/img')
time.sleep(1)
elem.click()

time.sleep(5)
browser.quit()
