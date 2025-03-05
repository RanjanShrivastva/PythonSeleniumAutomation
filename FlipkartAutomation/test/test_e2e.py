# import time
import time

from page_objects.HomePage import HomePage
from page_objects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_login_with_valid_username(self):
        loginpage = LoginPage(self.driver)
        time.sleep(5)
        loginpage.set_username("Admin")
        loginpage.set_password("admin123")
        time.sleep(5)
        loginpage.click_on_login()
        time.sleep(5)
        # homepage = HomePage(self.driver)
        # tct = homepage.get_search_content()
        # for i in tct:
        #     print(i)

    # def test_verify_home_page(self):
    #     homepage.get_company_name()
    #     homepage.get_user_name()
    #     tct = homepage.get_search_content()
    #     for i in tct:
    #         print(i)

    # def test_check(self):
    #     print("Hello")
    #     time.sleep(20)
