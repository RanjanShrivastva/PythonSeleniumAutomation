from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from selenium.webdriver.common.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(executable_path='D:\\Softwares\\Drivers\\chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
select_xpath = driver.find_element(By.ID, 'dropdown-class-example')
drp_down = Select(select_xpath)
drp_down.select_by_value('option1')
time.sleep(5)
drp_down.select_by_index(2)
time.sleep(5)