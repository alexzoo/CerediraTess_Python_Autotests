import configparser
from pathlib import Path

import allure
import pytest
from pytest import fixture

from helpers.files_helper import find_project_root, get_log_dir_path
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
    page.goto('https://www.avito.ru/penza/transport?cd=1')
    yield StartPage(page)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Hook for creating a screenshot when a test fails and attaching it to the Allure report.

    Args:
        item (pytest.Item): The test item.
        call (object): The hook call.

    Yields:
        object: The outcome of the hook call.

    """
    outcome = yield
    report = outcome.get_result()
    page = item.funcargs.get('page')
    if page and report.when == 'call' and report.failed:
        screenshot_path = f"screenshots/{item.nodeid.replace('::', '_').replace('/', '_')}.png"
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="screenshot", attachment_type=allure.attachment_type.PNG)


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    outcome = yield
    report = outcome.get_result()

    config_path = find_project_root(Path(__file__)) / 'config.ini'
    config = configparser.ConfigParser()
    config.read(config_path)
    log_file_path = get_log_dir_path() / config.get('logging', 'file_path', fallback='app.log')

    if report.when == 'call' and report.failed:
        if Path(log_file_path).exists():
            with open(log_file_path, 'r') as log_file:
                log_content = log_file.read()
            allure.attach(log_content, name="log_file", attachment_type=allure.attachment_type.TEXT)

