from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# To launch Browser
driver = webdriver.Chrome(executable_path='C:\\Ranjan\\Software\\Driver\\chromedriver_win32\\chromedriver.exe')
# driver = webdriver.Firefox(executable_path='C:\\Ranjan\\Software\\Driver\\geckodriver-v0.29.1-win64\\geckodriver.exe')
driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
driver.find_element_by_css_selector("#name").send_keys("Hello")
driver.find_element_by_id("alertbtn").click()
time.sleep(2)
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
assert "share this practice" in alert_text
alert.accept()
# To dismiss alert
# alert.dismiss()
driver.close()
