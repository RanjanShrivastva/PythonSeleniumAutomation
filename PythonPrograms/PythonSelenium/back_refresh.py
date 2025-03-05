from selenium import webdriver
import time
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Python\\Python37\\Scripts\\chromedriver.exe')
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com/recaptcha/api2/demo')
# driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
# driver.maximize_window()
# print('Title  is : ', driver.title)
# print('current url is :  ', driver.current_url)
# driver.back()
# driver.refresh()
# time.sleep(5)
captcha_class = '//div[@class="recaptcha-checkbox-border"]'
time.sleep(3)
# driver.find_element(By.CLASS_NAME, captcha_class).click()
driver.execute_script("argument[0].click();", captcha_class)
time.sleep(3)

driver.close()
