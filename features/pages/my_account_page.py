from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class MyAccountPage(BasePage):

    LOGOUT_OPTION = (By.LINK_TEXT, "Logout")
    MY_ACCOUNT_HEADING = (By.XPATH, "//h2[normalize-space()='My Account']")
    CHANGE_YOUR_PASSWORD = (By.LINK_TEXT, "Change your password")
    SUCCESS_ALERT_MSG = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def click_logout_option(self):
        self.wait_for_element_clickable(self.LOGOUT_OPTION).click()

    def is_account_page_displayed(self) -> bool:
        return self.is_displayed(self.MY_ACCOUNT_HEADING)

    def click_change_password_link(self):
        self.wait_for_element_clickable(self.CHANGE_YOUR_PASSWORD).click()

    def is_password_change_successful(self):
        alert = self.wait_for_element_visible(self.SUCCESS_ALERT_MSG)
        return "Success: Your password has been successfully updated." in alert.text