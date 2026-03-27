from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base_page import BasePage


class LoginPage(BasePage):

    EMAIL_ADDRESS_FIELD     = (By.ID, "input-email")
    PASSWORD_FIELD          = (By.ID, "input-password")
    LOGIN_BUTTON            = (By.XPATH, "//input[@value='Login']")
    FORGOTTEN_PASSWORD_LINK = (By.LINK_TEXT, "Forgotten Password")
    NEW_CUSTOMER_CONTINUE   = (By.XPATH, "//div[@class='well']//a[normalize-space()='Continue']")
    RIGHT_COLUMN_LOGIN      = (By.XPATH, "//a[@class='list-group-item'][normalize-space()='Login']")
    WARNING_MESSAGE         = (By.XPATH, "//div[contains(@class,'alert-danger')]")

    REGISTER_ACCOUNT_HEADING = (By.XPATH, "//h1[normalize-space()='Register Account']")
    CHANGE_PASSWORD_LINK    = (By.LINK_TEXT, "Change your password")
    PASSWORD_CONFIRM_FIELD  = (By.ID, "input-confirm")
    CONTINUE_BUTTON         = (By.XPATH, "//input[@value='Continue']")
    BREADCRUMB              = (By.XPATH, "//ul[@class='breadcrumb']")
    LOGIN_PAGE_HEADING      = (By.XPATH, "//h2[normalize-space()='Returning Customer']")

    def click_right_column_login(self):
        self.wait_for_element_visible(self.RIGHT_COLUMN_LOGIN).click()

    def enter_email(self, email: str):
        self.send_keys(self.EMAIL_ADDRESS_FIELD, email)

    def enter_password(self, password: str):
        self.send_keys(self.PASSWORD_FIELD, password)

    def clear_email(self):
        self.clear_field(self.EMAIL_ADDRESS_FIELD)

    def clear_password(self):
        self.clear_field(self.PASSWORD_FIELD)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, email: str, password: str):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def click_forgotten_password_link(self):
        self.click(self.FORGOTTEN_PASSWORD_LINK)

    def click_new_customer_continue(self):
        self.click(self.NEW_CUSTOMER_CONTINUE)

    def tab_to_field_and_type(self, locator: tuple, text: str):
        element = self.wait_for_element_visible(locator)
        element.send_keys(Keys.TAB)
        element.send_keys(text)

    def click_login_button_n_times(self, n: int):
        for attempt in range(n):
            self.click(self.LOGIN_BUTTON)

    def enter_new_password_and_confirm(self, new_password: str):
        self.send_keys(self.PASSWORD_FIELD, new_password)
        self.send_keys(self.PASSWORD_CONFIRM_FIELD, new_password)

    def click_continue_on_password_change(self):
        self.click(self.CONTINUE_BUTTON)


    def is_login_page_displayed(self) -> bool:
        return self.is_displayed(self.LOGIN_PAGE_HEADING)

    def is_warning_message_displayed(self) -> bool:
        return self.is_displayed(self.WARNING_MESSAGE)

    def get_warning_message_text(self) -> str:
        return self.get_text(self.WARNING_MESSAGE)

    def is_forgotten_password_link_displayed(self) -> bool:
        return self.is_displayed(self.FORGOTTEN_PASSWORD_LINK)

    def get_email_placeholder(self) -> str:
        return self.get_placeholder(self.EMAIL_ADDRESS_FIELD)

    def get_password_placeholder(self) -> str:
        return self.get_placeholder(self.PASSWORD_FIELD)

    def get_password_field_type(self) -> str:
        return self.get_input_type(self.PASSWORD_FIELD)

    def is_register_account_page_displayed(self) -> bool:
        return self.is_displayed(self.REGISTER_ACCOUNT_HEADING)

    def is_breadcrumb_displayed(self) -> bool:
        return self.is_displayed(self.BREADCRUMB)

    def get_login_page_url(self) -> str:
        return self.get_current_url()

    def get_login_page_title(self) -> str:
        return self.get_page_title()

    def tab_until_element(self, locator, max_tabs=30):
        target = self.driver.find_element(*locator)
        for attempt in range(max_tabs):
            active = self.driver.switch_to.active_element
            if active == target:
                return active
            active.send_keys(Keys.TAB)
        raise Exception(f"Could not reach element via Tab: {locator}")

    def enter_email_using_tab(self, email):
        field = self.tab_until_element(self.EMAIL_ADDRESS_FIELD)
        field.clear()
        field.send_keys(email)

    def enter_password_using_tab(self, password):
        field = self.tab_until_element(self.PASSWORD_FIELD)
        field.send_keys(password)

    def press_login_using_tab(self):
        button = self.tab_until_element(self.LOGIN_BUTTON)
        button.send_keys(Keys.ENTER)

    def is_user_still_logged_in_after_back(self):
        self.driver.refresh()
        self.wait_for_url_contains("account/account")
        return True

    def is_user_logged_out_after_back(self):
        self.driver.refresh()
        self.wait_for_url_contains("account/login")
        return True

    def is_login_failed(self):
        error = self.wait_for_element_visible(self.WARNING_MESSAGE)
        return (
                "Warning" in error.text and
                "account/login" in self.driver.current_url
        )