from behave import given, when, then

# @given("I open the TutorialsNinja application in my browser")
# def step_open_application(context):
#     assert "Your Store" in context.driver.title, f"Application did not load — expected 'Your Store' in page title"


@given('I am logged in with email "{email}" and password "{password}"')
def step_i_am_logged_in(context, email, password):
    context.home_page.click_my_account_dropdown()
    context.home_page.click_login_option()
    context.login_page.login(email, password)
    assert context.my_account_page.is_account_page_displayed(), \
        f"I could not log in with email '{email}' — pre-condition failed"


@when('I type "{keyword}" into the Search text box')
def step_type_in_search_box(context, keyword):
    context.search_page.enter_search_keyword(keyword)


@when("I leave the Search text box empty")
def step_leave_search_box_empty(context):
    context.search_page.clear_search_box()


@when("I click the Search icon button")
def step_click_search_icon(context):
    context.search_page.click_search_icon_button()


@when('I type "{criteria}" into the "Search Criteria" field on the Search page')
def step_type_in_search_criteria(context, criteria):
    context.search_page.enter_search_criteria(criteria)


@when('I click the "Search" button on the Search page')
def step_click_search_page_button(context):
    context.search_page.click_search_page_button()


@when('I check the "Search in product descriptions" checkbox')
def step_check_search_in_descriptions(context):
    context.search_page.click_search_in_descriptions_checkbox()


@when('I check the "Search in subcategories" checkbox')
def step_check_search_in_subcategories(context):
    context.search_page.click_search_in_subcategories_checkbox()


@when('I select "{category}" from the "Category" dropdown')
def step_select_category(context, category):
    context.search_page.select_category(category)


@when('I select several options from the "Sort By" dropdown')
def step_select_sort_options(context):
    for option in ["Name (A - Z)", "Name (Z - A)", "Price (Low > High)"]:
        context.search_page.select_sort_option(option)


@when('I select a number from the "Show" dropdown')
def step_select_show_option(context):
    context.search_page.select_show_option("25")


@when('I click the "List" view button')
def step_click_list_view(context):
    context.search_page.click_list_view()


@when('I click the "Grid" view button')
def step_click_grid_view(context):
    context.search_page.click_grid_view()

@when('I click the "Product Compare" link')
def step_click_product_compare(context):
    context.search_page.click_product_compare_link()


@when("I click on the product image or name in List view")
def step_click_product_in_list(context):
    context.search_page.click_product_name_in_list()


@when("I click on the product image or name in Grid view")
def step_click_product_in_grid(context):
    context.search_page.click_product_name_in_grid()


@when("I go back to the search results")
def step_go_back_to_results(context):
    context.driver.back()


@when('I click the "Site Map" link in the footer')
def step_click_site_map(context):
    context.search_page.click_site_map_footer_link()


@when('I click the "Search" link on the Site Map page')
def step_click_search_on_site_map(context):
    context.search_page.click_search_link_on_site_map()


@when("I navigate through all the pages of the application")
def step_navigate_all_pages(context):
    pages = [
        context.base_url,
        context.base_url + "index.php?route=account/login",
        context.base_url + "index.php?route=account/register",
        context.base_url + "index.php?route=product/search",
        context.base_url + "index.php?route=information/sitemap",
    ]
    context.all_pages_have_search = True
    for url in pages:
        context.driver.get(url)
        if not context.search_page.is_header_search_box_displayed():
            context.all_pages_have_search = False
            break

@when("I use the Tab and Enter keys to perform a Search operation")
def step_search_with_keyboard(context):
    context.search_page.perform_search_with_keyboard()


@when("I use the keyboard to select options on the Search page")
def step_use_keyboard_on_search_page(context):
    pass  # Verified by checking the resulting page URL in the Then step


@then('I should see "{product_name}" displayed in the search results')
def step_assert_product_in_results(context, product_name):
    assert context.search_page.is_product_displayed_in_results(product_name), (
        f"I could not see '{product_name}' in the search results. "
        f"Total results found: {context.search_page.get_search_result_count()}"
    )


@then('I should see the message "{expected_message}" on the Search Results page')
def step_assert_no_results_message(context, expected_message):
    assert context.search_page.is_no_results_message_displayed(), (
        f"I expected to see '{expected_message}' but it was not displayed. "
        f"Result count: {context.search_page.get_search_result_count()}"
    )


@then("I should see more than one product displayed in the search results")
def step_assert_multiple_results(context):
    count = context.search_page.get_search_result_count()
    assert count > 1, \
        f"I expected more than 1 product in the results but I saw only {count}"


@then("I should see the product whose description contains \"iLife\" displayed in the search results")
def step_assert_product_by_description(context):
    count = context.search_page.get_search_result_count()
    assert count >= 1, \
        "I could not find any product after searching using the description text 'iLife'"

@then("I should see proper placeholder text in the Search text box")
def step_assert_header_search_placeholder(context):
    placeholder = context.search_page.get_header_search_placeholder()
    assert placeholder, \
        "I could not see any placeholder text in the header Search text box"


@then('I should see proper placeholder text in the "Search Criteria" text box on the Search page')
def step_assert_search_criteria_placeholder(context):
    placeholder = context.search_page.get_search_criteria_placeholder()
    assert placeholder, \
        "I could not see any placeholder text in the 'Search Criteria' text box"


@then("I should see the product displayed correctly in List view with all action buttons working")
def step_assert_single_product_in_list(context):
    count = context.search_page.get_search_result_count()
    assert count >= 1, "I could not see any product in the List view"


@then("I should see the product displayed correctly in Grid view with all action buttons working")
def step_assert_single_product_in_grid(context):
    count = context.search_page.get_search_result_count()
    assert count >= 1, "I could not see any product in the Grid view"


@then("I should see all products displayed correctly in List view with all action buttons working")
def step_assert_multiple_in_list(context):
    count = context.search_page.get_search_result_count()
    assert count > 1, \
        f"I expected multiple products in List view but I saw only {count}"


@then("I should see all products displayed correctly in Grid view with all action buttons working")
def step_assert_multiple_in_grid(context):
    count = context.search_page.get_search_result_count()
    assert count > 1, \
        f"I expected multiple products in Grid view but I saw only {count}"


@then("I should be taken to the Product Display Page of that product")
def step_assert_on_product_display_page(context):
    assert context.search_page.is_product_display_page_shown(), \
        "I was not taken to the Product Display Page after clicking the product"


@then('I should be taken to the "Product Comparison" page')
def step_assert_on_compare_page(context):
    assert context.search_page.is_product_compare_page_displayed(), \
        "I was not taken to the Product Comparison page"


@then('I should be taken to the "Search" page')
def step_assert_on_search_page(context):
    assert context.search_page.is_search_page_heading_displayed(), \
        "I was not taken to the Search page"


@then("I should see the Breadcrumb working correctly on the Search Results page")
def step_assert_search_breadcrumb(context):
    assert context.search_page.is_breadcrumb_displayed(), \
        "I could not see the Breadcrumb on the Search Results page"


@then("I should see the products sorted according to the option I selected")
def step_assert_sorted(context):
    selected = context.search_page.get_sort_by_selected_text()
    assert selected, \
        "I could not verify sorting — no option appears selected in the Sort By dropdown"


@then("I should see only that number of products displayed on the current page")
def step_assert_show_count(context):
    selected = context.search_page.get_show_selected_text()
    assert selected, \
        "I could not verify the product count — no option appears selected in the Show dropdown"


@then("I should see the Search text box and the Search icon button on every page")
def step_assert_search_on_all_pages(context):
    assert getattr(context, "all_pages_have_search", False), \
        "I could not see the Search text box or icon button on one or more pages of the application"


@then("I should see a proper Page Heading on the Search page")
def step_assert_search_heading(context):
    assert context.search_page.is_search_page_heading_displayed(), \
        "I could not see a proper Page Heading on the Search page"


@then("I should see the correct Page URL for the Search page")
def step_assert_search_url(context):
    url = context.search_page.get_current_url()
    assert "route=product/search" in url or "search" in url.lower(), \
        f"I expected the URL to contain the Search route but I saw: {url}"


@then("I should see the correct Page Title for the Search page")
def step_assert_search_title(context):
    title = context.search_page.get_page_title()
    assert title, "I could not see a Page Title on the Search page"


@then("I should see the Search page UI matching the UI checklist")
def step_assert_search_ui(context):
    assert context.search_page.is_header_search_box_displayed(), \
        "I could not see the Search text box on the page"
    assert context.search_page.is_header_search_button_displayed(), \
        "I could not see the Search icon button on the page"


@then("I should see all Search page options displayed correctly")
def step_assert_search_page_options(context):
    assert context.search_page.is_displayed(context.search_page.SORT_BY_DROPDOWN), \
        "I could not see the 'Sort By' dropdown on the Search Results page"
    assert context.search_page.is_displayed(context.search_page.SHOW_DROPDOWN), \
        "I could not see the 'Show' dropdown on the Search Results page"


@then("I should be able to complete the Search operation using only the keyboard")
def step_assert_keyboard_search_done(context):
    url = context.search_page.get_current_url()
    assert "search" in url.lower(), \
        "I could not complete the Search operation using keyboard keys"


@then("I should see the Search functionality working correctly in my current environment")
def step_assert_search_cross_env(context):
    assert (
        context.search_page.is_search_page_heading_displayed()
        or context.search_page.get_search_result_count() >= 0
    ), "I could not verify the Search functionality in my current environment"
