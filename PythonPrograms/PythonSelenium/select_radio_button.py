from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(executable_path='D:\\Softwares\\Drivers\\chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, '//input[@value="radio1"]').click()
# driver.find_element_by_xpath('//input[@value="radio1"]').click()
time.sleep(5)
