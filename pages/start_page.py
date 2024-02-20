import allure
from playwright.sync_api import Page

from elements.base_element import BaseElement
from elements.button import Button
from pages._base_page import BasePage
from pages.search_page import SearchPage


class StartPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.popup_close_button = Button(self.page.locator('form button[type="button"]'))
        self.all_categories_button = Button(self.page.locator('button[data-marker="top-rubricator/all-categories"]'))
        self.categories = BaseElement(self.page.locator('div[class*="new-rubricator-content-rootCategory__text"]'))
        self.subcategories = BaseElement(self.page.locator('div[class*="new-rubricator-content-child-"]'))

    @allure.step("Close popup window")
    def close_popup(self) -> None:
        self.popup_close_button.click()

    @allure.step("Select category and subcategory")
    def select_category_and_subcategory(self, category_name: str, subcategory_name: str) -> None:
        self.close_popup()
        self.all_categories_button.click()
        self.categories.get_by_text(category_name).first.hover()
        self.subcategories.get_by_text(subcategory_name).first.click()

    @allure.step("Go to search page")
    def goto_search_page(self) -> SearchPage:
        return SearchPage(self.page)
