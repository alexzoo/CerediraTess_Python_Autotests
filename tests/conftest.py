import configparser
import random
from datetime import datetime
from pathlib import Path

import allure
import pytest
from pytest import fixture

from helpers.files_helper import find_project_root, get_dir_path
from pages.start_page import StartPage


@fixture
def page(playwright):
    """
    Creates a new page for the test.

    Args:
        playwright (Playwright): Playwright test automation library.

    Returns:
        context (Context): Playwright browser context.
    """
    browser = playwright.chromium.launch(
        headless=True,
        args=[
            '--start-maximized',
            '--no-sandbox',
            '--disable-dev-shm-usage'
        ]

    )
    # maximize the browser window
    context = browser.new_context(no_viewport=True)

    return context.new_page()


@fixture()
def start_page(page):
    page.open_page('https://www.avito.ru/penza/transport?cd=1')
    yield StartPage(page)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Hook for creating a screenshot when a test fails and attaching it to the Allure report.

    Args:
        item (pytest.Item): The test item.

    Yields:
        object: The outcome of the hook call.
    """
    outcome = yield
    report = outcome.get_result()
    page = item.funcargs.get('page')
    if page and report.when == 'call' and report.failed:
        test_name = item.name[:15]
        current_time = datetime.now().strftime("%H%M%S")
        random_number = random.randint(10, 99999)
        screenshot_file_name = f"{test_name}_{current_time}_{random_number}.png"
        screenshots_dir = get_dir_path('screenshots')
        screenshot_path = screenshots_dir / screenshot_file_name
        page.screenshot(path=str(screenshot_path))
        allure.attach.file(str(screenshot_path), name="screenshot", attachment_type=allure.attachment_type.PNG)


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    """
    This function is a hook implementation for pytest. It is triggered after each test is run and provides
    an opportunity to attach additional information to the test report.

    Args:
        report (pytest.runner.TestReport): The test report object that contains information about the
            test run.

    This function checks if the test failed and if so, it attaches the log file content to the Allure report.
    The log file content is retrieved from the log file path specified in the configuration file and attached
    as a text file.

    The function uses the following imports:
    - pytest.runner: This module provides the TestReport class, which is used to access information about the
        test run.
    - allure: This module is used to attach files and other artifacts to the Allure report.
    - configparser: This module is used to read the configuration file.
    - os.path: This module provides the Path class, which is used to construct the log file path.
    """
    outcome = yield
    report = outcome.get_result()

    config_path = find_project_root(Path(__file__)) / 'config.ini'
    config = configparser.ConfigParser()
    config.read(config_path)
    log_file_path = get_dir_path('logs') / config.get('logging', 'log_file', fallback='app.log')

    if report.when == 'call' and report.failed:
        if Path(log_file_path).exists():
            with open(log_file_path, 'r') as log_file:
                log_content = log_file.read()
            allure.attach(log_content, name="log_file", attachment_type=allure.attachment_type.TEXT)
