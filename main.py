from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from io import BytesIO
from PIL import Image
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
time.sleep(2)
driver.get("https://row1.vfsglobal.com/GlobalAppointment/Account/RegisteredLogin")

#Login

driver.find_element_by_id('EmailId').send_keys('kayes.fuad@northsouth.edu') #Email
driver.find_element_by_id('Password').send_keys('@Kayes321') #password

#Take screenshot

image = driver.find_element_by_id('CaptchaImage').screenshot_as_png
im = Image.open(BytesIO(image))  # uses PIL library to open image in memory
im.save('captcha.png')

#Load Image


#Captch Solver
driver.find_element_by_id('CaptchaInputText').send_keys("") #captcha
time.sleep(5)

driver.find_element_by_xpath('//*[@id="ApplicantListForm"]/div[4]').click()

driver.find_element_by_xpath('//*[@id="Accordion1"]/div/div[2]/div/ul/li[1]').click()

#Select Location
ddelement= Select(driver.find_element_by_id('LocationId'))
ddelement.select_by_index(6)

#Select Visa Category
ddelement= Select(driver.find_element_by_id('VisaCategoryId'))
ddelement.select_by_index(1)

driver.find_element_by_id('btnContinue').click() #Visa Page button click

#Add Customer
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[3]/a').click()

#Passport Number
driver.find_element_by_id('PassportNumber').send_keys("BN3240242")


#Date of Birth
driver.find_element_by_id('DateOfBirth').send_keys("11011998")

#Passport Expiry Date
driver.find_element_by_id('PassportExpiryDate').send_keys("01012025")


#Select Nationality Id
ddelement= Select(driver.find_element_by_id('NationalityId'))
ddelement.select_by_visible_text('BANGLADESH')

#Select Nationality Id
ddelement= Select(driver.find_element_by_id('GenderId'))
ddelement.select_by_visible_text('Male')


#Button Click

driver.find_element(By.ID, 'submitbuttonId').click()
accept = driver.switch_to.alert
accept.accept()

#OTP
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="ApplicantListForm"]/div[2]').click()
time.sleep(30)

driver.find_element_by_id('txtsub').click()

driver.find_element_by_id('btnContinueService').click()

time.sleep(5)

driver.find_element_by_xpath("//div[@class='fc-day fc-wed fc-widget-content fc-future' and style='background-color: rgb(255, 150, 202); cursor: pointer;']")

time.sleep(5)

driver.find_element_by_css_selector("input[type='radio'][value='xUc2m4DGouH7OxZSdHnSfqXhFube1hrRw4luyX2FSZA=']").click()

time.sleep(5)

driver.find_element_by_id('ReachVFS').click()
driver.find_element_by_id('IAgree').click()

driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()


