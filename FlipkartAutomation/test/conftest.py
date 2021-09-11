import pytest
from selenium import webdriver

driver_path_chrome = 'C:\\Projects\\FlipkartAutomation\\drivers\\chromedriver.exe'
driver_path_ff = 'C:\\Projects\\FlipkartAutomation\\drivers\\geckodriver.exe'
driver_path_ie = 'C:\\Projects\\FlipkartAutomation\\drivers\\'
app_url = 'https://flipkart.com'


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
        driver = webdriver.Chrome(executable_path=driver_path_chrome)
        driver.get(app_url)
    elif browser_name.lower() == 'ff' or 'firefox':
        driver = webdriver.Chrome(executable_path=driver_path_ff)
    driver.get(app_url)
    driver.maximize_window()
    # return driver
    request.cls.driver = driver
    yield
    driver.close()
