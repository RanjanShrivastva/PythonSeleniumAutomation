class HomePage:
    def __init__(self, driver):
        self.driver = driver

    text_company_name_xpath = '//img[@class="_2xm1JU"]'
    text_user_name_xpath = '//*[@class="exehdJ"]'
    # text_search_content_name = '//*[@name="q"]'
    text_search_content_name = 'q'

    def get_company_name(self):
        company_name = self.driver.find_element_by_xpath(self.text_company_name_xpath).text
        print(company_name)
        # assert company_name == "Flipkart"

    def get_user_name(self):
        user_name = self.driver.find_element_by_xpath(self.text_user_name_xpath).text
        # assert user_name == "Ranjan"

    def get_search_content(self):
        search_content = self.driver.find_element_by_name(self.text_search_content_name).text
        return search_content
        # assert search_content == "Search for products, brands and more"
