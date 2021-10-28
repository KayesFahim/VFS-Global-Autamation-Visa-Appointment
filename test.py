import cv2
import numpy as np
import pytesseract
from PIL import Image
img = Image.open('captcha.png').convert('L')
img.save('captcha.png')

#Load Image
pytesseract.pytesseract.tesseract_cmd =r'C:\Users\Hp\anaconda3\envs\SeleniumPy\Library\bin\tesseract.exe'
text = pytesseract.image_to_string(img, lang='eng',
                        config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

print(text)