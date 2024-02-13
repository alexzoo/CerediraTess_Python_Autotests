import allure
from playwright.sync_api import Page

from elements.button import Button
from pages._base_page import BasePage
from pages.search_page import SearchPage


class StartPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.popup_close_button = Button(self.page.locator('//form//button[@type="button"]'))
        self.all_categories_btn = Button(self.page.locator('//button[@data-marker="top-rubricator/all-categories"]'))
        self.category_electronics = self.page.locator('//div[contains(@class, "new-rubricator-content-rootCategory__text") and contains(normalize-space(), "Электроника")]')
        self.category_orgtechnics_and_supplies = self.page.locator('//div[contains(@class, "new-rubricator-content-child")]/a[@data-name="Оргтехника и расходники"]')

    @allure.step("Close popup window")
    def close_popup(self) -> None:
        self.popup_close_button.click()

    @allure.step("Click 'All categories' button")
    def click_all_categories_btn(self) -> None:
        self.all_categories_btn.click()

    @allure.step("Hover 'Electronics' category")
    def hover_category_electronics(self) -> None:
        self.category_electronics.hover()

    @allure.step("Click 'Orgtechnics and supplies' category")
    def click_category_orgtechnics_and_supplies(self) -> None:
        self.category_orgtechnics_and_supplies.click()

    @allure.step("Go to 'Orgtechnics and supplies' page")
    def goto_search_page(self) -> SearchPage:
        self.close_popup()
        self.click_all_categories_btn()
        self.hover_category_electronics()
        self.click_category_orgtechnics_and_supplies()
        return SearchPage(self.page)
