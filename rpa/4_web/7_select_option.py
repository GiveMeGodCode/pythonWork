from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')
browser.switch_to.frame('iframeResult')

elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')

elem.click()

elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')

time.sleep(5)
