from time import sleep

from playwright.sync_api import Page
import allure

from elements.button import Button
from elements.input import Input
from pages._base_page import BasePage


class SearchPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.search_form_input = Input(self.page.locator('input[data-marker="search-form/suggest"]'))
        self.search_form_submit_button = Button(self.page.locator('button[data-marker="search-form/submit-button"]'))
        self.search_filters = self.page.locator('div[data-marker="search-filters"]')
        self.search_filters_submit_button = Button(self.page.locator('button[data-marker="search-filters/submit-button"]'))
        self.search_results = self.page.locator('div[data-marker="catalog-serp"]')
        self.change_location = self.page.locator('div[data-marker="search-form/change-location"]')
        self.popup_location = 'div[data-marker="popup-location/popup"]'
        self.popup_location_input = Button(self.page.locator('input[data-marker="popup-location/region/input"]'))
        self.suggest_list = self.page.locator('ul[data-marker="suggest-list"]')
        self.popup_location_save_button = Button(self.page.locator('button[data-marker="popup-location/save-button"]'))
        self.sort_title = self.page.locator('span[data-marker="sort/title"]')
        self.sort_dropdown = self.page.locator('div[data-marker="sort/dropdown"]')

    @allure.step("Search item")
    def make_search(self, item_name: str) -> None:
        self.search_form_input.click()
        self.search_form_input.fill(item_name)
        self.search_form_submit_button.click()
        self.page.wait_for_load_state()

    @allure.step("Apply search filter 'New'")
    def apply_search_filter_new(self, new=False) -> None:
        new_checkbox = self.search_filters.get_by_text("Новые")
        if new_checkbox.is_checked() != new:
            new_checkbox.click()
            assert new_checkbox.is_checked() == new
            self.search_filters_submit_button.click()
            self.page.wait_for_load_state()

    @allure.step("Change region")
    def change_region(self, region_name: str) -> None:
        self.change_location.click()
        self.change_location.click()
        self.page.wait_for_selector(self.popup_location)
        self.popup_location_input.fill(region_name)
        self.suggest_list.get_by_text(region_name).first.click()
        self.popup_location_save_button.click()
        self.page.wait_for_load_state()

    @allure.step("Sort results")
    def sort_results(self, sort_type: str) -> None:
        if sort_type not in ['Дороже', 'Дешевле', 'По дате']:
            raise ValueError("use only: 'Дороже', 'Дешевле' or 'По дате'")
        self.sort_title.first.click()
        self.sort_dropdown.get_by_text(sort_type).click()
        self.page.wait_for_load_state()

    @allure.step("Print prices for first five items")
    def print_prices_for_items(self, nums: int) -> None:
        for i in range(nums):
            list_of_prices = (self.search_results.locator('meta[itemprop="price"]').nth(i).get_attribute('content'))
            print(f"Price {list_of_prices}")

