from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from .config_reader import (
get_browser,
get_headless,
get_implicit_wait,
get_screenshot_dir
)

class DriverFactory:

    @staticmethod
    def get_driver(browser=None, headless=None, implicit_wait=None):

        browser = (browser or get_browser() or "chrome").lower()
        headless = headless if headless is not None else get_headless()
        implicit_wait = implicit_wait or get_implicit_wait()

        if browser == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            driver = webdriver.Chrome(options=options)

        elif browser == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)

        elif browser == "edge":
            options = EdgeOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Edge(options=options)

        else:
            raise ValueError(
                f"Unsupported browser: '{browser}'. "
                f"Supported values are: chrome, firefox, edge."
            )

        driver.implicitly_wait(implicit_wait)
        driver.maximize_window()
        driver.screenshot_dir = get_screenshot_dir()

        return driver