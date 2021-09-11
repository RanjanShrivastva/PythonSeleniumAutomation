from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# To launch Browser
driver = webdriver.Chrome(executable_path='C:\\Ranjan\\Software\\Driver\\chromedriver_win32\\chromedriver.exe')
# driver = webdriver.Firefox(executable_path='C:\\Ranjan\\Software\\Driver\\geckodriver-v0.29.1-win64\\geckodriver.exe')
driver.get('https://www.rahulshettyacademy.com/seleniumPractise/#/')
driver.maximize_window()
time.sleep(5)
driver.close()
