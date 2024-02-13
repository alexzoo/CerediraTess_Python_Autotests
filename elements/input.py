from playwright.sync_api import Locator
from ._base_element import BaseElement


class TextInput(BaseElement):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def label(self) -> str:
        return self.locator("label[class~='control-label']").text_content()

    @property
    def input(self) -> Locator:
        return self.locator("span[class~='text_input']>input")

    @property
    def error(self):
        return self.locator("span[class*='error']").text_content()

    def get_value(self) -> str:
        return self.input.input_value()


class SearchInput(BaseElement):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def input(self) -> Locator:
        return self.locator('input[data-marker="search-form/suggest"]')

    @property
    def button(self) -> Locator:
        return self.locator('button[data-marker="search-form/submit-button"]')

    @property
    def search_result(self):
        return self.locator('h1[data-marker="page-title/text"]')

    def search_item(self, item_name: str) -> None:
        self.input.click()
        self.input.fill(item_name)
        self.button.click()

