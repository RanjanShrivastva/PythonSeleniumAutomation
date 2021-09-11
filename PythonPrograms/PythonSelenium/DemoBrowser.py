from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path='C:\\Ranjan\\Software\\Driver\\chromedriver_win32\\chromedriver.exe')
# driver = webdriver.Firefox(executable_path='C:\\Ranjan\\Software\\Driver\\geckodriver-v0.29.1-win64\\geckodriver.exe')
driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
print('Title  is : ', driver.title)
print('current url is :  ', driver.current_url)
driver.back()
driver.refresh()
time.sleep(5)
driver.close()
