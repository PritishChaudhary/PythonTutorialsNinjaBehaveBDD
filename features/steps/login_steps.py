from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@given("I open the TutorialsNinja application in my browser")
def step_open_application(context):
    assert "Your Store" in context.driver.title, f"Application did not load — expected 'Your Store' in page title"

@when('I click on "My Account" dropmenu')
def step_click_my_account(context):
    context.home_page.click_my_account_dropdown()


@when('I click on "Login" option')
def step_click_login_option(context):
    context.home_page.click_login_option()

@when('I click on "Register" option')
def step_click_login_option(context):
    context.home_page.click_register_option()


@when('I click the "login page" link from the "Register Account" page')
def step_click_login_from_register(context):
    # context.login_page.navigate_to_login_via_register_page(context.base_url)
    context.home_page.go_to_register_page()
    context.register_page.click_login_page_link()


@when('I click the "Login" option from the "Right Column" navigation')
def step_click_right_column_login(context):
    context.login_page.click_right_column_login()


@when("I navigate back to the Login page")
def step_navigate_back_to_login(context):
    context.driver.back()
    context.home_page.go_to_login_page()


@when('I enter "{value}" into the "E-Mail Address" field')
def step_enter_email(context, value):
    context.login_page.enter_email(value)


@when('I enter "{value}" into the "Password" field')
def step_enter_password(context, value):
    context.login_page.enter_password(value)


@when('I leave the "E-Mail Address" field empty')
def step_leave_email_empty(context):
    context.login_page.clear_email()


@when('I leave the "Password" field empty')
def step_leave_password_empty(context):
    context.login_page.clear_password()


@when('I click the "Login" button')
def step_click_login_button(context):
    context.login_page.click_login_button()


@when('I click the "Login" button 5 times with the same invalid credentials')
def step_click_login_5_times(context):
    context.login_page.click_login_button_n_times(5)


@when('I click on the "Forgotten Password" link')
def step_click_forgotten_password(context):
    context.login_page.click_forgotten_password_link()


@when('I click the "Continue" button under the "New Customer" section')
def step_click_new_customer_continue(context):
    context.login_page.click_new_customer_continue()


@when('I press Tab to move to the "E-Mail Address" field and type "{email}"')
def step_tab_to_email(context, email):
    context.login_page.enter_email_using_tab(email)



@when('I press Tab to move to the "Password" field and type "{password}"')
def step_tab_to_password(context, password):
    context.login_page.enter_password_using_tab(password)


@when('I press Tab to move to the "Login" button and press Enter')
def step_tab_to_login_press_enter(context):
    context.login_page.press_login_using_tab()


@when('I type any text into the "Password" field')
def step_type_any_text_password(context):
    #Enter sample text into the Password field for security checks
    context.login_page.enter_password("SamplePassword123")


@when('I type "{text}" into the "Password" field')
def step_type_specific_text_password(context, text):
    context.login_page.enter_password(text)


@when('I select "Logout" from the dropdown')
def step_select_logout(context):
    context.home_page.click_my_account_dropdown()
    context.my_account_page.click_logout_option()


@when("I click the browser back button")
def step_click_back_button(context):
    context.driver.back()


@when('I click on the "Change your password" link')
def step_click_change_password(context):
    context.my_account_page.click_change_password_link()


@when('I enter "{new_password}" into the "Password" field and the "Password Confirm" field')
def step_enter_new_password_and_confirm(context, new_password):
    context.login_page.enter_new_password_and_confirm(new_password)


@when('I click the "Continue" button to save my new password')
def step_click_continue_password_change(context):
    context.login_page.click_continue_on_password_change()


@when("I navigate back to the application base URL")
def step_navigate_to_base_url(context):
    context.driver.get(context.base_url)


@when("I click on various navigation options available on the Login page")
def step_click_various_nav_options(context):
    context.home_page.go_to_login_page()


@then("I should be on the Login page")
def step_assert_on_login_page(context):
    page_title = context.driver.title
    assert page_title == "Account Login", f"Expected 'Account Login' but got '{page_title}'"


@then('I should be logged in and taken to the "Account" page')
def step_assert_on_account_page(context):
    assert context.my_account_page.is_account_page_displayed(), \
        "I was not logged in — the Account page heading was not found"


@then("I should not be able to log in to the application")
def step_assert_login_not_possible(context):
    assert context.login_page.is_login_failed(), \
        "I was unexpectedly logged in with inactive credentials"


@then("I should not be allowed to log in with my old password")
def step_assert_old_password_rejected(context):
    assert not context.my_account_page.is_account_page_displayed(), \
        "My old password was accepted — the password change did not work correctly"


@then('I should see a warning message "{expected_message}"')
def step_assert_warning_message(context, expected_message):
    assert context.login_page.is_warning_message_displayed(), \
        "I did not see any warning message on the page"
    actual = context.login_page.get_warning_message_text()
    assert expected_message in actual, (
        f"Warning message mismatch.\n"
        f"  I expected to see : {expected_message}\n"
        f"  I actually saw    : {actual}"
    )


@then('I should see the "Forgotten Password" link on the Login page')
def step_assert_forgotten_password_link_visible(context):
    assert context.login_page.is_forgotten_password_link_displayed(), \
        "I could not see the 'Forgotten Password' link on the Login page"


@then('I should be taken to the "Forgotten Password" page')
def step_assert_on_forgotten_password_page(context):
    assert context.login_page.is_forgotten_password_page_displayed(), \
        "I was not taken to the 'Forgotten Password' page"


@then('I should see proper placeholder text inside the "E-Mail Address" field')
def step_assert_email_placeholder(context):
    placeholder = context.login_page.get_email_placeholder()
    assert placeholder, \
        "I could not see any placeholder text in the 'E-Mail Address' field"


@then('I should see proper placeholder text inside the "Password" field')
def step_assert_password_placeholder(context):
    placeholder = context.login_page.get_password_placeholder()
    assert placeholder, \
        "I could not see any placeholder text in the 'Password' field"


@then("I should still be logged in and not be logged out")
def step_assert_still_logged_in(context):
    assert context.login_page.is_user_still_logged_in_after_back(), \
        "I was logged out after pressing the browser back button - I expected to remain logged in"


@then("I should not be logged in again")
def step_assert_not_logged_in_again(context):
    assert context.login_page.is_user_logged_out_after_back(), \
        "I was unexpectedly logged back in after pressing the browser back button post-logout"


@then('I should see my typed text hidden using masked characters in the "Password" field')
def step_assert_password_masked(context):
    field_type = context.login_page.get_password_field_type()
    assert field_type == "password", (
        f"I expected the Password field type to be 'password' but it was '{field_type}'"
    )


@then('the "Password" field input type should be "password" to prevent copying')
def step_assert_password_type_prevents_copy(context):
    field_type = context.login_page.get_password_field_type()
    assert field_type == "password", (
        f"I expected type='password' to prevent copying but found type='{field_type}'"
    )


@then('the "Password" field input type attribute should be "password" in the page source')
def step_assert_password_type_in_source(context):
    field_type = context.login_page.get_password_field_type()
    assert field_type == "password", \
        f"I expected type='password' in the page source but found type='{field_type}'"


@then('I should be taken to the "Register Account" page')
def step_assert_on_register_page(context):
    assert context.login_page.is_register_account_page_displayed(), \
        "I was not taken to the 'Register Account' page"


@then("I should be taken to the appropriate pages")
def step_assert_taken_to_appropriate_page(context):
    assert context.driver.title != "", \
        "I was not taken to any page after clicking the navigation option"


@then("I should see a proper Breadcrumb on the Login page")
def step_assert_login_breadcrumb(context):
    assert context.login_page.is_breadcrumb_displayed(), \
        "I could not see the Breadcrumb navigation on the Login page"


@then("I should see a proper Page Heading on the Login page")
def step_assert_login_heading(context):
    assert context.login_page.is_login_page_displayed(), \
        "I could not see a proper Page Heading on the Login page"


@then("I should see the correct Page URL for the Login page")
def step_assert_login_url(context):
    url = context.login_page.get_login_page_url()
    assert "account/login" in url, \
        f"I expected the URL to contain 'account/login' but I saw: {url}"


@then("I should see the correct Page Title for the Login page")
def step_assert_login_title(context):
    title = context.login_page.get_login_page_title()
    assert title, "I could not see a Page Title on the Login page"


@then("I should see the Login page UI matching the UI checklist")
def step_assert_login_ui(context):
    assert context.login_page.is_login_page_displayed(), \
        "I could not verify the Login page UI — Returning Customer section is missing"


@then('I should see the "Returning Customer" section with "E-Mail Address" and "Password" fields')
def step_assert_returning_customer_section(context):
    assert context.login_page.is_login_page_displayed(), \
        "I could not see the 'Returning Customer' section on the Login page"
    assert context.login_page.is_displayed(context.login_page.EMAIL_ADDRESS_FIELD), \
        "I could not see the 'E-Mail Address' field on the Login page"
    assert context.login_page.is_displayed(context.login_page.PASSWORD_FIELD), \
        "I could not see the 'Password' field on the Login page"


@then('I should see the "New Customer" section with a "Continue" button')
def step_assert_new_customer_section(context):
    assert context.login_page.is_displayed(context.login_page.NEW_CUSTOMER_CONTINUE), \
        "I could not see the 'New Customer' section with a Continue button on the Login page"


@then("I should see the Login functionality working correctly in my current environment")
def step_assert_login_works_in_env(context):
    assert context.login_page.is_login_page_displayed(), \
        "I could not see the Login page working correctly in my current environment"


@then("my login session should still be active and I should not be logged out")
def step_assert_session_active(context):
    context.home_page.click_my_account_dropdown()
    assert context.my_account_page.is_displayed(context.my_account_page.LOGOUT_OPTION), \
        "My login session was not maintained — I could not find the 'Logout' option in the dropdown"

@when('I login with valid credentials')
def step_login_with_valid_credentials(context):
    context.login_page.login(context.email, context.password)


