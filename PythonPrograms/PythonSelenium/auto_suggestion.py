from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(executable_path='D:\\Softwares\\Drivers\\chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
a_xpath = driver.find_element(By.ID, 'autocomplete')
a_xpath.click()
a_xpath.send_keys("ind")
time.sleep(2)
los = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
for x in los:
    print(x.text)
