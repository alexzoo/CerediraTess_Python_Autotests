import allure
from playwright.sync_api import Page

from pages._base_page import BasePage
from pages.search_page import SearchPage


class StartPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.popup_close_button = 'form button[type="button"]'
        self.all_categories_button = 'button[data-marker="top-rubricator/all-categories"]'
        self.categories = 'div[class*="new-rubricator-content-rootCategory__text"]'
        self.subcategories = 'div[class*="new-rubricator-content-child-"]'

    @allure.step("Close popup window")
    def close_popup(self) -> None:
        self.page.locator(self.popup_close_button).click()

    @allure.step("Select category and subcategory")
    def select_category_and_subcategory(self, category_name: str, subcategory_name: str) -> None:
        self.close_popup()
        self.page.locator(self.all_categories_button).click()
        self.page.locator(self.categories).get_by_text(category_name).hover()
        self.page.locator(self.subcategories).get_by_text(subcategory_name).click()

    @allure.step("Go to search page")
    def goto_search_page(self) -> SearchPage:
        return SearchPage(self.page)
