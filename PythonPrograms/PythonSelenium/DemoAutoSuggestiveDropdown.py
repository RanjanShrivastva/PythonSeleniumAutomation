from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# To launch Browser
driver = webdriver.Chrome(executable_path='C:\\Ranjan\\Software\\Driver\\chromedriver_win32\\chromedriver.exe')
# driver = webdriver.Firefox(executable_path='C:\\Ranjan\\Software\\Driver\\geckodriver-v0.29.1-win64\\geckodriver.exe')
driver.get('https://www.rahulshettyacademy.com/dropdownsPractise/')
driver.maximize_window()
time.sleep(2)
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)
# To locate and provide input
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
for country in countries:
    if country.text == "India":
        country.click()
        break
time.sleep(2)
driver.close()


