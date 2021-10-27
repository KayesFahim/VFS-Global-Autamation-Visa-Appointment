from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from PIL import Image
import pytesseract
import argparse
import cv2
from io import BytesIO
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
im.save('captch.png')

#Load Image

LoadImage = Image.open("captch.png")

# construct the argument parser and parse the arguments}
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
args = vars(ap.parse_args())

LoadImage = Image.open(args["captch.png"])
# use Tesseract to OCR the image
text = pytesseract.image_to_string(LoadImage)
print(text)

time.sleep(5)
#Captch Solver
driver.find_element_by_id('CaptchaInputText').send_keys("xyzzz") #captcha



