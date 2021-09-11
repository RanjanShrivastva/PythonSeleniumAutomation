from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# To launch Browser
driver = webdriver.Chrome(executable_path='C:\\Ranjan\\Software\\Driver\\chromedriver_win32\\chromedriver.exe')
# driver = webdriver.Firefox(executable_path='C:\\Ranjan\\Software\\Driver\\geckodriver-v0.29.1-win64\\geckodriver.exe')
driver.get('https://www.rahulshettyacademy.com/angularpractice/')
driver.maximize_window()

# To locate and provide input
driver.find_element_by_name("name").send_keys("hello")
driver.find_element_by_name("email").send_keys("hello@gmail.com")
# driver.find_element_by_id("exampleInputPassword1").send_keys("python")
driver.find_element_by_css_selector("[id='exampleInputPassword1']").send_keys("python")

driver.find_element_by_id("exampleCheck1").click()
gender_xpath = driver.find_element_by_id("exampleFormControlSelect1")
driver.find_element_by_xpath("//*[@type='submit']").click()

# To extract text values
extracted_text = driver.find_element_by_css_selector("[class*='alert']").text
print(extracted_text)
assert "success" in extracted_text

# To select values from drop down using select class
drop_down = Select(driver. find_element_by_css_selector("#exampleFormControlSelect1"))
drop_down.select_by_visible_text("Female")
# drop_down.select_by_index(0)
# To make delay or pause
time.sleep(5)
# To close browser
driver.close()
