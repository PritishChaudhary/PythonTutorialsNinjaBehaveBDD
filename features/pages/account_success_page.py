from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class AccountSuccessPage(BasePage):

    SUCCESS_HEADER = (By.XPATH, "//h1[text()='Your Account Has Been Created!']")
    CONTINUE_BTN = (By.XPATH, "//a[text()='Continue']")

    def is_account_created(self):
        header = self.wait_for_element_visible(self.SUCCESS_HEADER)
        return "Your Account Has Been Created!" in header.text

    def click_continue_btn(self):
        self.wait_for_element_clickable(self.CONTINUE_BTN).click()