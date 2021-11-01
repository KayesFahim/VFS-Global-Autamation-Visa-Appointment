from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
URL ='https://bdjobs.com'

driver.get(URL)
time.sleep(7)


url_elements = driver.find_elements_by_xpath("//a[@href]")
url_elements_list = []
for url_element in url_elements:
    url_elements_list.append(url_element.get_attribute("href"))
    print(url_elements_list)

driver.close()