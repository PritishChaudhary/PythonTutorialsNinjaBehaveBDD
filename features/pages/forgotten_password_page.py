from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class ForgottenPasswordPage(BasePage):

    FORGOTTEN_PWD_HEADING = (By.XPATH, "//h1[normalize-space()='Forgot Your Password?']")

    def is_forgotten_password_page_displayed(self) -> bool:
        return self.is_displayed(self.FORGOTTEN_PWD_HEADING)