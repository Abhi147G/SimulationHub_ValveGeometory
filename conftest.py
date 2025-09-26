import pytest
import os
import sys
from selenium import webdriver

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from pages.valve_design_page import ValveDesignPageSelenium

def pytest_addoption(parser):
    """Add custom CLI options for pytest"""
    parser.addoption("--selenium-browser", action="store", default="chrome", help="Selenium browser: chrome or firefox")
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")


@pytest.fixture(scope="function")
def driver(request):
    """Setup and teardown for Selenium WebDriver"""
    browser = request.config.getoption("--selenium-browser")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        from selenium.webdriver.firefox.options import Options
        options = Options()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    """Base URL for the Valve Design app"""
    return "https://experiments.simulationhub.com/valve-design"


@pytest.fixture
def valve_design_page(driver, base_url):
    """Return a ready-to-use ValveDesignPageSelenium object"""
    page = ValveDesignPageSelenium(driver)
    page.goto(base_url)
    return page
