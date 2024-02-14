from time import sleep

from playwright.sync_api import Page
import allure

from elements.search import SearchForm, SearchFilters
from pages._base_page import BasePage


class SearchPage(BasePage):

    CHECKBOX_NEW = '//span[contains(text(), "Новые")]'
    CHANGE_REGION_LINK = '//div[@data-marker="search-form/change-location"]'
    SEARCH_REGION_INPUT = '//input[@data-marker="popup-location/region/input"]'
    SHOW_RESULTS_BTN = '//button[@data-marker="popup-location/save-button"]'
    SORT_RESULTS_DROPDOWN = '//div[@data-marker="view-change"]/..//span[@data-marker="sort/title"]'
    SORT_OPTION_EXPENSIVE = '//button[@data-marker="sort/custom-option(2)"]'
    RESULT_ITEMS = '//div[@data-marker="catalog-serp"]/div[@data-marker="item"]'
    LIST_OF_PRICES = '//div[@data-marker="catalog-serp"]//meta[@itemprop="price"]'

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.search_form = SearchForm(self.page.locator('div[data-marker="search-form"]'))
        self.search_filters = SearchFilters(self.page.locator('div[data-marker="search-filters"]'))
        self.search_results = self.page.locator('div[data-marker="catalog-serp"]')
        self.sort = self.page.locator('data-marker="sort/title"')
        self.change_location = self.page.locator('div[data-marker="search-form/change-location"]')
        self.popup_location_input = self.page.locator('input[data-marker="popup-location/region/input"]')
        self.suggest_list = self.page.locator('ul[data-marker="suggest-list"]')
        self.popup_location_save_button = self.page.locator('button[data-marker="popup-location/save-button"]')

    @allure.step("Search item")
    def make_search(self, item_name: str) -> None:
        self.search_form.search_item(item_name)
        self.search_results.wait_for()

    @allure.step("Apply search filters")
    def apply_search_filters(self, **kwargs) -> None:

        if kwargs.get('New', False):
            self.search_filters.switch_new_checkbox(on=True)

    @allure.step("Change region")
    def change_region(self, region_name: str) -> None:
        self.change_location.click()
        self.popup_location_input.fill(region_name)
        self.suggest_list.get_by_text(region_name).nth(0).click()
        # self.popup_location_save_button.wait_for()
        self.popup_location_save_button.click()



    @allure.step("Show results")
    def show_results(self) -> None:
        self.page.locator(self.SHOW_RESULTS_BTN).click()
        # wait for results to load
        self.page.wait_for_selector(self.RESULT_ITEMS)

    @allure.step("Sort results")
    def sort_results(self) -> None:
        # self.page.wait_for_selector(self.SORT_RESULTS_DROPDOWN)
        sleep(1)
        self.page.locator(self.SORT_RESULTS_DROPDOWN).click()
        self.page.wait_for_selector(self.SORT_OPTION_EXPENSIVE)
        self.page.locator(self.SORT_OPTION_EXPENSIVE).click()

    @allure.step("Print prices for first five items")
    def print_prices_for_items(self) -> None:
        for i in range(5):
            print(f"Цена {self.page.locator(self.LIST_OF_PRICES).nth(i).get_attribute('content')}")


