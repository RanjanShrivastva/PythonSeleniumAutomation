class LoginPage:
    textbox_username_xpath = "//input[@class='_2IX_2- VJZDxU']"
    textbox_password_xpath = "//*[@type='password']"
    button_submit_xpath = '//button[@class="_2KpZ6l _2HKlqd _3AWRsL"]'

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element_by_xpath(self.textbox_username_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def click_on_login(self):
        self.driver.find_element_by_xpath(self.button_submit_xpath).click()