from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from webdriver_manager.chrome import ChromeDriverManager

# To launch Browser
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(executable_path='D:\\Softwares\\Drivers\\chromedriver.exe')
# driver = webdriver.Firefox(executable_path='C:\\Ranjan\\Software\\Driver\\geckodriver-v0.29.1-win64\\geckodriver.exe')
driver.get('https://www.rahulshettyacademy.com/seleniumPractise/#/')
driver.maximize_window()
time.sleep(5)
driver.close()
