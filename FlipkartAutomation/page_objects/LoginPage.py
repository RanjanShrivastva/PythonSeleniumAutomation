class LoginPage:
    textbox_username_xpath = "//input[@name='username']"
    textbox_password_xpath = "//input[@name='password']"
    button_submit_xpath = "//button[@type='submit']"

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
