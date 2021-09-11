from selenium import webdriver
from selenium.webdriver import ActionChains
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

ff_driver_path = 'C:\\Ranjan\\Software\\Driver\\geckodriver-v0.29.1-win64\\geckodriver.exe'
chrome_driver_path = 'C:\\Ranjan\\Software\\Driver\\chromedriver_win32\\chromedriver.exe'

opt = Options()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/71.0.3578.98 Safari/537.36'
opt.add_argument('user-agent={0}'.format(user_agent))
opt.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.delete_all_cookies()

# driver = webdriver.Chrome(executable_path='C:\\Ranjan\\Software\\Driver\\chromedriver_win32\\chromedriver.exe')
# driver = webdriver.Firefox(executable_path='C:\\Ranjan\\Software\\Driver\\geckodriver-v0.29.1-win64\\geckodriver.exe')
driver.get('https://www.nseindia.com/')
driver.maximize_window()
market_dat_xpath = driver.find_element_by_xpath("//a[contains(text(),'Market Data')]").click()
# action = ActionChains(driver)
# action.move_to_element(market_dat_xpath)
time.sleep(2)
driver.find_element_by_xpath("//a[contains(text(),'Equity & SME Market')]").click()
# action.move_to_element(equity_sme_market_xpath).click()
equity_drop_down_xpath = driver.find_element_by_id('equitieStockSelect')
select = Select(equity_drop_down_xpath)
