from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):

    # common locators across multiple pages
    MY_ACCOUNT_DROPMENU = (By.XPATH, "//span[normalize-space()='My Account']")
    REGISTER_OPTION = (By.PARTIAL_LINK_TEXT, "Register")
    LOGIN_OPTION = (By.LINK_TEXT, "Login")
    SEARCH_BOX_FIELD     = (By.NAME, "search")
    SEARCH_BUTTON        = (By.XPATH, "//div[@id='search']//button[@type='button']")

    def click_my_account_dropdown(self):
        self.wait_for_element_clickable(self.MY_ACCOUNT_DROPMENU).click()

    def click_login_option(self):
        self.wait_for_element_clickable(self.LOGIN_OPTION).click()

    def click_register_option(self):
        self.wait_for_element_clickable(self.REGISTER_OPTION).click()

    def go_to_login_page(self):
        self.click_my_account_dropdown()
        self.click_login_option()

    def go_to_register_page(self):
        self.click_my_account_dropdown()
        self.click_register_option()

    # Action methods — Search Bar
    def enter_search_keyword(self, keyword: str):
        self.send_keys(self.SEARCH_BOX_FIELD, keyword)

    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)

    def search_for(self, keyword: str):
        self.enter_search_keyword(keyword)
        self.click_search_button()

    def is_home_page_displayed(self) -> bool:
        return self.is_displayed(self.SEARCH_BOX_FIELD)

    def is_search_box_displayed(self) -> bool:
        return self.is_displayed(self.SEARCH_BOX_FIELD)

    def is_search_button_displayed(self) -> bool:
        return self.is_displayed(self.SEARCH_BUTTON)

    def get_search_box_placeholder(self) -> str:
        return self.get_placeholder(self.SEARCH_BOX_FIELD)
