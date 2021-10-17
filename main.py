from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://visa.vfsglobal.com/ind/en/deu/login")
wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div")))



driver.find_element(By.id("mat-input-0")).send_keys("Abc@gmail.com")

