import allure
from playwright.sync_api import Page
from pages._base_page import BasePage
from pages.search_page import SearchPage


# Locators
popup_close_button = 'css=form button[type="button"]'
all_categories_button = 'css=button[data-marker="top-rubricator/all-categories"]'
categories = 'css=div[class*="new-rubricator-content-rootCategory__text"]'
subcategories = 'css=div[class*="new-rubricator-content-child-"]'


class StartPage(BasePage):
    page_url = '/penza/transport?cd=1'

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @allure.step("Close popup window")
    def close_popup(self) -> None:
        self.page.locator(popup_close_button).click()

    @allure.step("Select category and subcategory")
    def select_category_and_subcategory(self, category_name: str, subcategory_name: str) -> None:
        self.close_popup()
        self.page.locator(all_categories_button).click()
        self.page.locator(categories).get_by_text(category_name).first.hover()
        self.page.locator(subcategories).get_by_text(subcategory_name).first.click()

    @allure.step("Go to search page")
    def goto_search_page(self) -> SearchPage:
        return SearchPage(self.page)
