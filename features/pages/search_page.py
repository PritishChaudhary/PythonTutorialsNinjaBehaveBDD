from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage


class SearchPage(BasePage):

    HEADER_SEARCH_BOX       = (By.NAME, "search")
    HEADER_SEARCH_ICON_BTN  = (By.XPATH, "//div[@id='search']//button[@type='button']")

    NO_RESULTS_MESSAGE      = (By.XPATH, "//p[contains(text(),'There is no product that matches the search criteria')]")
    SEARCH_RESULT_PRODUCTS  = (By.XPATH, "//div[@id='content']//div[contains(@class,'product-thumb')]")
    PRODUCT_NAMES_IN_RESULTS = (By.XPATH, "//div[@id='content']//h4/a")

    SEARCH_CRITERIA_FIELD   = (By.ID, "input-search")
    SEARCH_IN_DESC_CHECKBOX = (By.ID, "description")
    SEARCH_IN_SUBCATEGORIES_CHECKBOX = (By.XPATH, "//input[@name='sub_category']")
    CATEGORY_DROPDOWN       = (By.XPATH, "//select[@name='category_id']")
    SEARCH_PAGE_BUTTON      = (By.ID, "button-search")

    SORT_BY_DROPDOWN        = (By.ID, "input-sort")
    SHOW_DROPDOWN           = (By.ID, "input-limit")

    LIST_VIEW_BUTTON        = (By.ID, "list-view")
    GRID_VIEW_BUTTON        = (By.ID, "grid-view")

    PRODUCT_IMAGE_IN_LIST   = (By.XPATH, "//div[contains(@class,'product-list')]//img")
    PRODUCT_NAME_IN_LIST    = (By.XPATH, "//div[contains(@class,'product-list')]//h4/a")
    PRODUCT_IMAGE_IN_GRID   = (By.XPATH, "//div[contains(@class,'product-grid')]//img")
    PRODUCT_NAME_IN_GRID    = (By.XPATH, "//div[contains(@class,'product-grid')]//h4/a")

    PRODUCT_DISPLAY_HEADING = (By.XPATH, "//div[@id='content']//h1")

    PRODUCT_COMPARE_LINK    = (By.ID, "compare-total")
    PRODUCT_COMPARE_HEADING = (By.XPATH, "//h1[normalize-space()='Product Comparison']")

    BREADCRUMB              = (By.XPATH, "//ul[@class='breadcrumb']")

    SITE_MAP_FOOTER_LINK    = (By.LINK_TEXT, "Site Map")
    SITE_MAP_SEARCH_LINK    = (By.LINK_TEXT, "Search")

    SEARCH_PAGE_HEADING     = (By.XPATH, "//h1[contains(text(),'Search')]")


    def enter_search_keyword(self, keyword: str):
        self.send_keys(self.HEADER_SEARCH_BOX, keyword)

    def clear_search_box(self):
        self.clear_field(self.HEADER_SEARCH_BOX)

    def click_search_icon_button(self):
        self.click(self.HEADER_SEARCH_ICON_BTN)

    def enter_search_criteria(self, criteria: str):
        self.send_keys(self.SEARCH_CRITERIA_FIELD, criteria)

    def click_search_page_button(self):
        self.click(self.SEARCH_PAGE_BUTTON)

    def click_search_in_descriptions_checkbox(self):
        self.check_checkbox(self.SEARCH_IN_DESC_CHECKBOX)

    def click_search_in_subcategories_checkbox(self):
        self.check_checkbox(self.SEARCH_IN_SUBCATEGORIES_CHECKBOX)

    def select_category(self, category_name: str):
        self.select_dropdown_by_visible_text(self.CATEGORY_DROPDOWN, category_name)

    def select_sort_option(self, sort_text: str):
        self.select_dropdown_by_visible_text(self.SORT_BY_DROPDOWN, sort_text)

    def select_show_option(self, show_value: str):
        self.select_dropdown_by_visible_text(self.SHOW_DROPDOWN, show_value)


    def click_list_view(self):
        self.click(self.LIST_VIEW_BUTTON)

    def click_grid_view(self):
        self.click(self.GRID_VIEW_BUTTON)

    def click_product_image_in_list(self):
        self.click(self.PRODUCT_IMAGE_IN_LIST)

    def click_product_name_in_list(self):
        self.click(self.PRODUCT_NAME_IN_LIST)

    def click_product_image_in_grid(self):
        self.click(self.PRODUCT_IMAGE_IN_GRID)

    def click_product_name_in_grid(self):
        self.click(self.PRODUCT_NAME_IN_GRID)


    def click_product_compare_link(self):
        self.click(self.PRODUCT_COMPARE_LINK)


    def click_site_map_footer_link(self):
        self.click(self.SITE_MAP_FOOTER_LINK)

    def click_search_link_on_site_map(self):
        self.click(self.SITE_MAP_SEARCH_LINK)


    def perform_search_with_keyboard(self):
        search_box = self.wait_for_element_visible(self.HEADER_SEARCH_BOX)
        search_box.send_keys("HP")
        search_box.send_keys(Keys.RETURN)


    def get_search_result_count(self) -> int:
        try:
            return self.get_elements_count(self.SEARCH_RESULT_PRODUCTS)
        except Exception:
            return 0

    def is_no_results_message_displayed(self) -> bool:
        return self.is_displayed(self.NO_RESULTS_MESSAGE)

    def is_product_displayed_in_results(self, product_name: str) -> bool:
        try:
            elements = self.get_all_elements(self.PRODUCT_NAMES_IN_RESULTS)
            for el in elements:
                if product_name.lower() in el.text.lower():
                    return True
            return False
        except Exception:
            return False

    def get_header_search_placeholder(self) -> str:
        return self.get_placeholder(self.HEADER_SEARCH_BOX)

    def get_search_criteria_placeholder(self) -> str:
        return self.get_placeholder(self.SEARCH_CRITERIA_FIELD)

    def get_sort_by_selected_text(self) -> str:
        return self.get_selected_dropdown_text(self.SORT_BY_DROPDOWN)

    def get_show_selected_text(self) -> str:
        return self.get_selected_dropdown_text(self.SHOW_DROPDOWN)

    def is_product_display_page_shown(self) -> bool:
        return self.is_displayed(self.PRODUCT_DISPLAY_HEADING)

    def is_product_compare_page_displayed(self) -> bool:
        return self.is_displayed(self.PRODUCT_COMPARE_HEADING)

    def is_breadcrumb_displayed(self) -> bool:
        return self.is_displayed(self.BREADCRUMB)

    def is_search_page_heading_displayed(self) -> bool:
        return self.is_displayed(self.SEARCH_PAGE_HEADING)

    def is_header_search_box_displayed(self) -> bool:
        return self.is_displayed(self.HEADER_SEARCH_BOX)

    def is_header_search_button_displayed(self) -> bool:
        return self.is_displayed(self.HEADER_SEARCH_ICON_BTN)
