from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from PIL import Image
import pytesseract
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
"""
change source & destination station prior to run like Humsafar starts with PNBE and sanghmitra starts from DNR
change date as specified format
"""
username_list = ['r973830862', 'surbhillb']
username = username_list[0]
password_list = ['rkumar1433', 'Surbhi2024@@@']
password = password_list[0]
class_type_list = ['Sleeper (SL)', 'AC 3 Tier (3A)']
class_type = class_type_list[1]
train_name_list = [' SANGHA MITRA EX (12296)', ' HUMSAFAR EXP (22353)']
train_name = train_name_list[0]
date_str = 'Sun, 28 Jul'
src_station = 'DANAPUR - DNR '
dest_station = 'SMVT BENGALURU - SMVB '
target_time = "10:00:03"    # Specify the time threshold in 24-hour format (HH:MM)


# Define Chrome options
chrome_options = Options()
chrome_options.add_argument("--force-device-scale-factor=0.7")
chrome_options.add_experimental_option("detach", True)
driver_obj = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver_obj, 60)
# driver_obj.implicitly_wait(5)
driver_obj.get("https://www.irctc.co.in/nget/train-search")
driver_obj.maximize_window()
driver_obj.find_element("xpath", "//a[contains(text(),'LOGIN')]").click()
# time.sleep(2)
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='userid']")))
driver_obj.find_element("xpath", "//input[@formcontrolname='userid']").send_keys("{}".format(username))
time.sleep(1)
driver_obj.find_element("xpath", "//input[@formcontrolname='password']").send_keys("{}".format(password))
# time.sleep(2)
# wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='captcha-img']")))
# captcha_lg1 = driver_obj.find_element("xpath", "//img[@class='captcha-img']")
# captcha_lg1.screenshot("captcha1.png")
# # img to txt generator
# pytesseract.pytesseract.tesseract_cmd = r'C:\\OCR\\Tesseract-OCR\\tesseract.exe'  # your path may be different
# img1 = Image.open('captcha1.png')
# text1 = pytesseract.image_to_string(img1)
# print("first captcha: ", text1)
time.sleep(10)
# driver_obj.find_element("xpath", "//input[@id='captcha']").send_keys(text1)
# driver_obj.find_element("xpath", "//*[contains(text(), 'SIGN IN')]").click()
# logic to wait for home page
# wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@aria-controls='pr_id_1_list']")))
driver_obj.find_element("xpath", "//input[@aria-controls='pr_id_1_list']").send_keys("{}".format(src_station))
driver_obj.find_element("xpath", "//label[contains(text(), 'BOOK TICKET')]").click()
driver_obj.find_element("xpath", "//input[@aria-controls='pr_id_2_list']").send_keys("{}".format(dest_station))
driver_obj.find_element("xpath", "//label[contains(text(), 'BOOK TICKET')]").click()
# time.sleep(2)
wait.until(EC.visibility_of_element_located((By.XPATH, "//p-calendar[@dateformat='dd/mm/yy']//child::span")))
driver_obj.find_element("xpath", "//p-calendar[@dateformat='dd/mm/yy']//child::span").click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='{}']".format(date_str[5:7]))))
driver_obj.find_element("xpath", "//a[text()='{}']".format(date_str[5:7])).click()
driver_obj.find_element("id", "journeyClass").click()
# time.sleep(1)
# wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='AC 3 Tier (3A)']")))
wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='{}']".format(class_type))))
driver_obj.find_element("xpath", "//span[text()='{}']".format(class_type)).click()
driver_obj.find_element("id", "journeyQuota").click()
driver_obj.find_element("xpath", "//span[text()='TATKAL']").click()
driver_obj.find_element("xpath", "//button[@type='submit']").click()
# time.sleep(1)
###############################################################################
"""Wait until the current time reaches the target time."""
while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    print(current_time)
    if current_time >= target_time:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), '{}')]/ancestor::div/following-sibling::div[4]//*[contains(text(), '{}')]/parent::div/following-sibling::div".format(train_name, class_type))))
        driver_obj.find_element("xpath", "//strong[contains(text(), '{}')]/ancestor::div/following-sibling::div[4]//*[contains(text(), '{}')]/parent::div/following-sibling::div".format(train_name, class_type)).click()
        # time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), '{}')]/ancestor::div/following-sibling::div[6]//*[@class='pre-avl']//*[contains(text(),'{}')]".format(train_name, date_str))))
        driver_obj.find_element("xpath", "//strong[contains(text(), '{}')]/ancestor::div/following-sibling::div[6]//*[@class='pre-avl']//*[contains(text(),'{}')]".format(train_name, date_str)).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btnDefault train_Search ng-star-inserted']")))
        driver_obj.find_element("xpath", "//button[@class='btnDefault train_Search ng-star-inserted']").click()
        # time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Passenger Name']")))
        driver_obj.find_element("xpath", "//input[@placeholder='Passenger Name']").send_keys("SURBHI KUMARI")
        driver_obj.find_element("xpath", "//input[@placeholder='Age']").send_keys("27")
        select_element = driver_obj.find_element("xpath", "//select[@formcontrolname='passengerGender']")
        select = Select(select_element)
        select.select_by_value('F')
        # to get confirm ticket only
        driver_obj.find_element("xpath", "//*[contains(text(), 'Book only if confirm berths are allotted.')]").click()
        driver_obj.find_element("xpath", "//p-radiobutton[@name='paymentType' and @id='2']").click()
        driver_obj.find_element("xpath", "//button[@class='train_Search btnDefault']").click()
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btnDefault train_Search']")))
        captcha_lg2 = driver_obj.find_element("xpath", "//img[@class='captcha-img']")
        captcha_lg2.screenshot("captcha2.png")
        img2 = Image.open('captcha2.png')
        text2 = pytesseract.image_to_string(img2)
        print("second captcha: ", text2)
        driver_obj.find_element("xpath", "//input[@id='captcha']").send_keys(text2)
        driver_obj.find_element("xpath", "//button[@class='btnDefault train_Search']").click()
        time.sleep(2)
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'BHIM/ UPI/ USSD')]")))
        driver_obj.find_element("xpath", "//span[contains(text(), 'BHIM/ UPI/ USSD')]").click()
        driver_obj.find_element("xpath", "//span[contains(text(), 'Pay using BHIM (Powered by PAYTM ) also accepts UPI ')]").click()
        driver_obj.find_element("xpath", "//button[contains(text(), 'Pay & Book ') and @class='btn btn-primary hidden-xs ng-star-inserted']").click()
        print(f"Current time ({current_time}) has reached the threshold ({target_time}). Proceeding with Selenium script.")
        break
    time.sleep(1)  # Check every 30 seconds




