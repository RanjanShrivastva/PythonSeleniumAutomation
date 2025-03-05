import pytest
from selenium import webdriver

driver_path_chrome = 'D:\\Projects\\PythonSeleniumAutomation\\FlipkartAutomation\\drivers\\chromedriver.exe'
driver_path_ff = 'D:\\Projects\\PythonSeleniumAutomation\\FlipkartAutomation\\drivers\\geckodriver.exe'
driver_path_ie = 'D:\\Projects\\PythonSeleniumAutomation\\FlipkartAutomation\\drivers\\'
app_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
        # "--browser_name", action="store", default="ff"
    )


@pytest.fixture(scope="class")
# @pytest.fixture(scope="function")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name.lower() == 'chrome':
        driver = webdriver.Chrome()
        driver.get(app_url)
    elif browser_name.lower() == 'ff' or 'firefox':
        driver = webdriver.Chrome()
    driver.get(app_url)
    driver.maximize_window()
    # return driver
    request.cls.driver = driver
    yield
    driver.close()
