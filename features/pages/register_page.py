from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class RegisterAccountPage(BasePage):

    LOGIN_PAGE_LINK = (By.LINK_TEXT, "login page")
    FIRST_NAME = (By.ID, "input-firstname")
    LAST_NAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    TELEPHONE = (By.ID, "input-telephone")
    PASSWORD = (By.ID, "input-password")
    CNF_PASSWORD = (By.ID, "input-confirm")
    AGREE_CHECKBOX = (By.NAME, "agree")
    CONTINUE_BTN = (By.XPATH, "//input[@value='Continue']")

    def click_login_page_link(self):
        self.wait_for_element_clickable(self.LOGIN_PAGE_LINK).click()

    def register_user(self, first_name, last_name, email, telephone, password, cnf_password):
        self.wait_for_element_visible(self.FIRST_NAME).send_keys(first_name)
        self.wait_for_element_visible(self.LAST_NAME).send_keys(last_name)
        self.wait_for_element_visible(self.EMAIL).send_keys(email)
        self.wait_for_element_visible(self.TELEPHONE).send_keys(telephone)
        self.wait_for_element_visible(self.PASSWORD).send_keys(password)
        self.wait_for_element_visible(self.CNF_PASSWORD).send_keys(cnf_password)
        self.wait_for_element_clickable(self.AGREE_CHECKBOX).click()
        self.wait_for_element_clickable(self.CONTINUE_BTN).click()