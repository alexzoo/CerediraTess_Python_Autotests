import pytest
from pytest import fixture
from pages.start_page import StartPage


@pytest.fixture()
def page(playwright):
    browser = playwright.chromium.launch(
        headless=False,
        args=[
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
