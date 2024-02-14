from playwright.sync_api import Locator
from ._base_element import BaseElement


class SearchForm(BaseElement):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    @property
    def input(self) -> Locator:
        return self.locator('input[data-marker="search-form/suggest"]')

    @property
    def button(self) -> Locator:
        return self.locator('button[data-marker="search-form/submit-button"]')

    # @property
    # def search_results(self):
    #     return self.locator('h1[data-marker="page-title/text"]')

    def search_item(self, item_name: str) -> None:
        self.input.click()
        self.input.fill(item_name)
        self.button.click()


class SearchFilters(BaseElement):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    def switch_new_checkbox(self, on=False) -> None:
        new_checkbox = self.get_by_text("Новые")
        if new_checkbox.is_checked() != on:
            new_checkbox.click()
