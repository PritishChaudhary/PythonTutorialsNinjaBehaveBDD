from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class ChangePasswordPage(BasePage):

    PASSWORD = (By.ID, "input-password")
    CNF_PASSWORD = (By.ID, "input-confirm")
    CONTINUE_BTN = (By.XPATH, "//input[@value='Continue']")

    def change_password(self, password):
        self.wait_for_element_clickable(self.PASSWORD).send_keys(password)
        self.wait_for_element_clickable(self.CNF_PASSWORD).send_keys(password)
        self.wait_for_element_clickable(self.CONTINUE_BTN).click()