from time import sleep

from playwright.sync_api import Page
import allure


class OrgtechnicsAndSuppliesPage:
    # locators
    SEARCH_FIELD = '//input[@data-marker="search-form/suggest"]'
    SEARCH_BTN = '//button[@data-marker="search-form/submit-button"]'
    CHECKBOX_NEW = '//span[contains(text(), "Новые")]'
    CHANGE_REGION_LINK = '//div[@data-marker="search-form/change-location"]'
    SEARCH_REGION_INPUT = '//input[@data-marker="popup-location/region/input"]'
    SHOW_RESULTS_BTN = '//button[@data-marker="popup-location/save-button"]'
    SORT_RESULTS_DROPDOWN = '//div[@data-marker="view-change"]/..//span[@data-marker="sort/title"]'
    SORT_OPTION_EXPENSIVE = '//button[@data-marker="sort/custom-option(2)"]'
    RESULT_ITEMS = '//div[@data-marker="catalog-serp"]/div[@data-marker="item"]'
    LIST_OF_PRICES = '//div[@data-marker="catalog-serp"]//meta[@itemprop="price"]'

    def __init__(self, page: Page) -> None:
        self.page = page

    @allure.step("Search item")
    def search_item(self, item_name: str) -> None:
        # self.page.locator(self.SEARCH_FIELD).clear()
        sleep(1)
        self.page.locator(self.SEARCH_FIELD).fill(item_name)
        sleep(1)
        self.page.locator(self.SEARCH_FIELD).press('Enter')
        # wait for results to load
        self.page.wait_for_selector(self.RESULT_ITEMS)

    @allure.step("Click 'New' checkbox")
    def click_checkbox_new(self) -> None:
        # self.page.wait_for_selector(self.CHECKBOX_NEW)
        sleep(1)
        self.page.locator(self.CHECKBOX_NEW).click()

    @allure.step("Change region")
    def change_region(self, region_name: str) -> None:
        self.page.locator(self.CHANGE_REGION_LINK).click()
        self.page.locator(self.SEARCH_REGION_INPUT).fill(region_name)
        self.page.locator(self.SEARCH_REGION_INPUT).press('Enter')

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
    def print_prices_for_first_five_items(self) -> None:
        for i in range(5):
            print(f"Цена {self.page.locator(self.LIST_OF_PRICES).nth(i).get_attribute('content')}")


