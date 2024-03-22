from playwright.sync_api import Page


class BasePage:
    base_url = 'https://www.avito.ru'
    page_url = None

    def __init__(self, page: Page) -> None:
        self.page = page

    def open_page(self) -> None:
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Base page can not be opened')
