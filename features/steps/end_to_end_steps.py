import time
import uuid

from behave import when, then


@when('I register a new user')
def step_register_user(context):
    first_name = "Test"
    last_name = "User"
    email = f"test{uuid.uuid4().hex[:6]}@mail.com"
    telephone = "9999999999"
    password = "12345"
    cnf_password = "12345"

    # store in context for reuse later
    context.email = email
    context.password = password
    context.cnf_password = cnf_password

    context.register_page.register_user(
        first_name,
        last_name,
        email,
        telephone,
        password,
        cnf_password
    )

    assert context.account_success_page.is_account_created()
    context.account_success_page.click_continue_btn()
    context.my_account_page.click_logout_option()

@when('I change my password')
def step_change_password(context):
    new_password = f"NewPass@{int(time.time())}"
    context.new_password = new_password
    context.my_account_page.click_change_password_link()
    context.change_password_page.change_password(new_password)
    assert context.my_account_page.is_password_change_successful()

@when('I logout')
def step_logout(context):
    context.my_account_page.click_logout_option()

@then('I should not be able to login with old password')
def step_verify_old_password(context):
    context.home_page.go_to_login_page()
    context.login_page.login(context.email, context.password)
    assert context.login_page.is_login_failed(), "Login should have failed but didn't"

@then('I should be able to login with new password')
def step_verify_new_password(context):
    context.home_page.go_to_login_page()
    context.login_page.login(context.email, context.new_password)
    assert context.my_account_page.is_account_page_displayed()