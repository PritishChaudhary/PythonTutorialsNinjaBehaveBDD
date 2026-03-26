from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver, explicit_wait: int = 20):
        self.driver = driver
        self.wait = WebDriverWait(driver, explicit_wait)

    #Navigation helpers
    def open(self, url: str):
        self.driver.get(url)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_page_title(self) -> str:
        return self.driver.title

    def go_back(self):
        self.driver.back()

    def refresh(self):
        self.driver.refresh()

    # Wait helpers
    def wait_for_element_visible(self, locator: tuple):
        #Wait until the element is visible in the DOM and return it
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Element not visible: {locator}"
        )

    def wait_for_element_clickable(self, locator: tuple):
        #Wait until the element is clickable and return it
        return self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element not clickable: {locator}"
        )

    def wait_for_element_present(self, locator: tuple):
        #Wait until the element is present in the DOM and return it
        return self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Element not present in DOM: {locator}"
        )

    def wait_for_url_contains(self, partial_url: str):
        #Wait until the current URL contains the given string
        self.wait.until(
            EC.url_contains(partial_url),
            message=f"URL does not contain: {partial_url}"
        )

    def wait_for_title_contains(self, partial_title: str):
        #Wait until the page title contains the given string
        self.wait.until(
            EC.title_contains(partial_title),
            message=f"Page title does not contain: {partial_title}"
        )

    # Interaction helpers
    def click(self, locator: tuple):
        element = self.wait_for_element_clickable(locator)
        element.click()

    def send_keys(self, locator: tuple, text: str):
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)

    def clear_field(self, locator: tuple):
        element = self.wait_for_element_visible(locator)
        element.clear()

    def press_enter(self, locator: tuple):
        element = self.wait_for_element_visible(locator)
        element.send_keys(Keys.ENTER)

    def press_tab(self, locator: tuple):
        element = self.wait_for_element_visible(locator)
        element.send_keys(Keys.TAB)

    def tab_and_type(self, locator: tuple, text: str):
        element = self.wait_for_element_visible(locator)
        element.send_keys(Keys.TAB)
        element.send_keys(text)

    def hover(self, locator: tuple):
        element = self.wait_for_element_visible(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def hover_and_click(self, hover_locator: tuple, click_locator: tuple):
        element = self.wait_for_element_visible(hover_locator)
        ActionChains(self.driver).move_to_element(element).perform()
        self.click(click_locator)


    # Dropdown helpers
    def select_dropdown_by_visible_text(self, locator: tuple, text: str):
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )
        dropdown = Select(element)
        for option in dropdown.options:
            if option.text.strip() == text:
                option.click()
                return
        raise Exception(f"Option '{text}' not found in dropdown")

    def select_dropdown_by_value(self, locator: tuple, value: str):
        element = self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Dropdown not present: {locator}"
        )
        Select(element).select_by_value(value)

    def get_selected_dropdown_text(self, locator: tuple) -> str:
        element = self.wait_for_element_visible(locator)
        return Select(element).first_selected_option.text


    # Assertion helpers
    def get_text(self, locator: tuple) -> str:
        #Wait for element to be visible and return its text content
        element = self.wait_for_element_visible(locator)
        return element.text.strip()

    def get_attribute(self, locator: tuple, attribute: str) -> str:
        #Return the value of a given attribute on the located element
        element = self.wait_for_element_present(locator)
        return element.get_attribute(attribute)

    def get_placeholder(self, locator: tuple) -> str:
        #Return the placeholder attribute value of an input field
        return self.get_attribute(locator, "placeholder")

    def get_input_type(self, locator: tuple) -> str:
        #Return the type attribute of an input field (e.g., 'password', 'text')
        return self.get_attribute(locator, "type")

    def is_displayed(self, locator: tuple) -> bool:
        #Return True if the element is present and visible on the page
        try:
            element = self.wait_for_element_visible(locator)
            return element.is_displayed()
        except Exception:
            return False

    def is_element_present(self, locator: tuple) -> bool:
        #Return True if the element exists in the DOM (may not be visible)
        try:
            self.wait_for_element_present(locator)
            return True
        except Exception:
            return False

    def get_elements_count(self, locator: tuple) -> int:
        #Return the number of elements matching the given locator
        from selenium.webdriver.support import expected_conditions as EC
        elements = self.wait.until(
            EC.presence_of_all_elements_located(locator),
            message=f"No elements found for: {locator}"
        )
        return len(elements)

    def get_all_elements(self, locator: tuple):
        #Return all elements matching the given locator as a list
        from selenium.webdriver.support import expected_conditions as EC
        return self.wait.until(
            EC.presence_of_all_elements_located(locator),
            message=f"No elements found for: {locator}"
        )


    # Checkbox helpers
    def check_checkbox(self, locator: tuple):
        #Check a checkbox if it is not already checked
        element = self.wait_for_element_clickable(locator)
        if not element.is_selected():
            element.click()

    def is_checkbox_selected(self, locator: tuple) -> bool:
        #Return True if the checkbox is currently selected
        element = self.wait_for_element_present(locator)
        return element.is_selected()

    def take_screenshot(self, file_path: str):
        self.driver.save_screenshot(file_path)
