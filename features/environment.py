import os
import datetime
import sys

from features.pages.account_success_page import AccountSuccessPage
from features.pages.change_password_page import ChangePasswordPage
from features.pages.my_account_page import MyAccountPage
from features.pages.register_page import RegisterAccountPage

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from features.utils.config_reader import (
    get_browser, get_headless, get_base_url,
    get_implicit_wait, get_explicit_wait, get_screenshot_dir
)
from features.utils.driver_factory import DriverFactory
from features.pages.home_page import HomePage
from features.pages.login_page import LoginPage
from features.pages.search_page import SearchPage


def before_scenario(context, scenario):
    context.base_url       = get_base_url()
    context.browser        = get_browser()
    context.headless       = get_headless()
    context.implicit_wait  = get_implicit_wait()
    context.explicit_wait  = get_explicit_wait()
    context.screenshot_dir = get_screenshot_dir()

    # Create driver per scenario
    context.driver = DriverFactory.get_driver(
        browser=context.browser,
        headless=context.headless,
        implicit_wait=context.implicit_wait
    )

    context.driver.get(context.base_url)

    # Init pages
    context.home_page   = HomePage(context.driver, context.explicit_wait)
    context.login_page  = LoginPage(context.driver, context.explicit_wait)
    context.search_page = SearchPage(context.driver, context.explicit_wait)
    context.my_account_page = MyAccountPage(context.driver, context.explicit_wait)
    context.register_page = RegisterAccountPage(context.driver, context.explicit_wait)
    context.change_password_page = ChangePasswordPage(context.driver, context.explicit_wait)
    context.account_success_page = AccountSuccessPage(context.driver, context.explicit_wait)

    os.makedirs(context.screenshot_dir, exist_ok=True)

def after_scenario(context, scenario):
    if scenario.status == "failed":
        timestamp       = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name       = scenario.name.replace(" ", "_").replace("/", "-")[:80]
        filename        = f"FAILED_{safe_name}_{timestamp}.png"
        screenshot_path = os.path.join(context.screenshot_dir, filename)

        context.driver.save_screenshot(screenshot_path)

    # Quit driver after each scenario
    if context.driver:
        context.driver.quit()