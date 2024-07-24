from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
# from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path='D:\\Softwares\\Drivers\\chromedriver.exe')
driver.implicitly_wait(0.5)
driver.get('https://www.rahulshettyacademy.com/dropdownsPractise/')
driver.maximize_window()
time.sleep(2)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, 'ctl00_mainContent_btn_FindFlights')))

drp_element = driver.find_element_by_xpath('//*[@id="ctl00_mainContent_ddl_originStation1"]')
slct = Select(drp_element)
time.sleep(2)
slct.select_by_index(2)
slct.select_by_value('BLR')
time.sleep(5)
act = ActionChains(driver)
act.move_to_element().perform()
# driver.window_handles
# driver.switch_to.frame
# driver.switch.alert
# driver.execute_script("document.getElementById()").send_keys("abc")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight()")
driver.execute_script("window.scrollBy(0, 200)")
# driver.get_screenshot_as_file("c:\\ranjan.jpg")

driver.close()

