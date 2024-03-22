import random
from datetime import datetime
import allure
import pytest
from pytest import fixture
from helpers.files_helper import get_dir_path


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

