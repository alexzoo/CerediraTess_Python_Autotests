import allure
from playwright.sync_api import Page

from elements.button import Button
from pages._base_page import BasePage
from pages.search_page import SearchPage


class StartPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.popup_close_button = Button(self.page.locator('form button[type="button"]'))
        self.all_categories_button = Button(self.page.locator('button[data-marker="top-rubricator/all-categories"]'))
        self.categories = self.page.locator('div[class*="new-rubricator-content-rootCategory__text"]')
        self.subcategories = self.page.locator('div[class*="new-rubricator-content-child-"]')

    @allure.step("Close popup window")
    def close_popup(self) -> None:
        self.popup_close_button.click()

    @allure.step("Select category and subcategory")
    def select_category_and_subcategory(self, category_name: str, subcategory_name: str) -> None:
        self.all_categories_button.click()
        categories = self.categories
        category_name = categories.get_by_text(category_name)
        category_name.hover()
        subcategory_name = self.subcategories.get_by_text(subcategory_name)
        subcategory_name.click()

    @allure.step("Go to search page")
    def goto_search_page(self) -> SearchPage:
        return SearchPage(self.page)
