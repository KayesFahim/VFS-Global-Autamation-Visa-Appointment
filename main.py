from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from io import BytesIO
from PIL import Image
import time
import easyocr
import imaplib
import email
import html2text
import re
import json



#Web driver Init
driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
String_Url ='https://row1.vfsglobal.com/GlobalAppointment/Account/RegisteredLogin?q=shSA0YnE4pLF9Xzwon/x/EpJs2NIweLgQQ8d+rbZm2FGx5CHm/l3tpvUMzs2dkBUvzmr37Un+1CH0C4/6fHwqQ=='
driver.get(String_Url)

#Login
driver.find_element_by_id('EmailId').send_keys('mrfawbd@gmail.com') #Email
driver.find_element_by_id('Password').send_keys('@Kayes321') #password

#Take screenshot
image = driver.find_element_by_id('CaptchaImage').screenshot_as_png
im = Image.open(BytesIO(image)).convert('L')  # uses PIL library to open image in memory
im.save('captcha.png')

#Load Image and convert into text
reader = easyocr.Reader(['en'], gpu=True, model_storage_directory='')
output = reader.readtext('captcha.png', detail = 0)
captchtext = ' '.join(map(str, output))
finalCaptchText = re.escape(captchtext.upper())

#Captch Solver
driver.find_element_by_id('CaptchaInputText').send_keys("") #captcha

time.sleep(8)
driver.find_element_by_xpath('//*[@id="ApplicantListForm"]/div[4]').click() #Click Login Button

#Click Appointments
driver.find_element_by_xpath('//*[@id="Accordion1"]/div/div[2]/div/ul/li[1]').click()

#Select Location
ddelement= Select(driver.find_element_by_id('LocationId'))
ddelement.select_by_index(6)

#Select Visa Category
ddelement= Select(driver.find_element_by_id('VisaCategoryId'))
ddelement.select_by_index(1)

driver.find_element_by_id('btnContinue').click() #Visa Page button click


for i in range(0, 5):
    #Add Customer
    driver.find_element_by_link_text('Add Customer').click()   
    driver.find_element_by_id('PassportNumber').send_keys("BN32400426"+str(i))
    driver.find_element_by_id('DateOfBirth').send_keys("11011998")
    driver.find_element_by_id('PassportExpiryDate').send_keys("01012025")
    ddelement= Select(driver.find_element_by_id('NationalityId'))
    ddelement.select_by_visible_text('BANGLADESH')
    driver.find_element_by_id('Mobile').clear()
    driver.find_element_by_id('Mobile').send_keys('1685370455')
    ddelement= Select(driver.find_element_by_id('GenderId'))
    ddelement.select_by_visible_text('Male')
    #Button Click
    driver.find_element(By.ID, 'submitbuttonId').click()
    accept = driver.switch_to.alert
    accept.accept()
    


#OTP
driver.find_element(By.XPATH, '//*[@id="ApplicantListForm"]/div[2]').click() #OTP send

time.sleep(30)
#OTP reading
host = 'imap.gmail.com'
username = 'mrfawbd@gmail.com'
password = '@Kayes321'


def get_inbox():
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("INBOX")
    _, search_data = mail.search(None,'(UNSEEN)', '(SUBJECT "OTP Confirmation Email")')
    my_message = []
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        # print(data[0])
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode()
        my_message.append(email_data)
    return my_message


if __name__ == "__main__":
    my_inbox = get_inbox()
    h = html2text.HTML2Text()
    h.ignore_links = True
    listToStr = ' '.join(map(str, my_inbox))
    PlainText = h.handle(listToStr)
    result = json.dumps(PlainText)
    getOTP = re.findall('\d+', result)
    finalOTP = ' '.join(map(str, getOTP))


time.sleep(5)    
#OTP
driver.find_element_by_id('OTPe').send_keys(finalOTP) #captcha

driver.find_element_by_id('txtsub').click()


driver.find_element_by_id('btnContinueService').click()

#driver.find_element_by_css_selector("div[style='background-color: rgb(188, 237, 145); cursor: pointer;']")
#driver.find_element_by_css_selector("input[type='radio'][value='xUc2m4DGouH7OxZSdHnSfqXhFube1hrRw4luyX2FSZA=']").click()

time.sleep(10)
driver.find_element_by_id('ReachVFS').click()
driver.find_element_by_id('IAgree').click()

driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
