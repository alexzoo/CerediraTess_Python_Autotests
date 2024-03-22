from playwright.sync_api import Page, expect
import allure
from pages._base_page import BasePage


# Locators
search_form_input = 'css=input[data-marker="search-form/suggest"]'
search_form_submit_button = 'css=button[data-marker="search-form/submit-button"]'
search_filters = 'css=div[data-marker="search-filters"]'
search_filters_submit_button = 'css=button[data-marker="search-filters/submit-button"]'
search_results = 'css=div[data-marker="catalog-serp"]'
change_location = 'css=div[data-marker="search-form/change-location"]'
# self.popup_location = 'css=div[data-marker="popup-location/popup"]'
popup_location_input = 'css=input[data-marker="popup-location/region/input"]'
suggest_list = 'css=ul[data-marker="suggest-list"]'
popup_location_save_button = 'css=button[data-marker="popup-location/save-button"]'
sort_title = 'css=span[data-marker="sort/title"]'
sort_dropdown = 'css=div[data-marker="sort/dropdown"]'
meta_locator = 'css=meta[itemprop="price"]'


class SearchPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @allure.step("Search item")
    def make_search(self, item_name: str) -> None:
        self.page.locator(search_form_input).click()
        self.page.locator(search_form_input).fill(item_name)
        self.page.locator(search_form_submit_button).click()
        self.page.wait_for_load_state()

    @allure.step("Apply search filters")
    def apply_search_filter(self, filter_name: str, checked: bool) -> None:
        filter_checkbox = self.page.locator(search_filters).get_by_text(filter_name)
        if filter_checkbox.is_checked() != checked:
            filter_checkbox.click()
            expect(filter_checkbox).to_be_checked(checked=checked)

        self.page.locator(search_filters_submit_button).click()
        self.page.wait_for_load_state()

    @allure.step("Change region")
    def change_region(self, region_name: str) -> None:

        for i in range(3):
            self.page.locator(change_location).click()
            if self.page.locator(popup_location_input).is_visible():
                break

        self.page.locator(popup_location_input).fill(region_name)
        self.page.locator(suggest_list).get_by_text(region_name).first.click()
        self.page.locator(popup_location_save_button).click()
        self.page.wait_for_load_state()

    @allure.step("Sort results")
    def sort_results(self, sort_type: str) -> None:
        if sort_type not in ['Дороже', 'Дешевле', 'По дате']:
            raise ValueError("use only: 'Дороже', 'Дешевле' or 'По дате'")

        for i in range(3):
            self.page.locator(sort_title).first.click()
            if self.page.locator(sort_dropdown).is_visible():
                break

        self.page.locator(sort_dropdown).get_by_text(sort_type).click()
        expect(self.page.locator(sort_title).first).to_contain_text(sort_type)
        self.page.wait_for_load_state()

    @allure.step("Print prices for first five items")
    def print_prices_for_items(self, nums: int) -> None:
        for i in range(nums):
            list_of_prices = self.page.locator(search_results).locator(meta_locator).nth(i).get_attribute('content')
            print(f"Price {list_of_prices}")
