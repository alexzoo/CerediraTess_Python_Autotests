import allure
from playwright.sync_api import Page
from pages.orgtechnics_and_supplies_page import OrgtechnicsAndSuppliesPage


class StartPage:
    # Locators
    POPUP_CLOSE_BUTTON = '//form//button[@type="button"]'
    ALL_CATEGORIES_BTN = '//button[@data-marker="top-rubricator/all-categories"]'
    CATEGORY_ELECTRONICS = '//div[contains(@class, "new-rubricator-content-rootCategory__text") and contains(normalize-space(), "Электроника")]'
    CATEGORY_ORGTECHNICS_AND_SUPPLIES = '//div[contains(@class, "new-rubricator-content-child")]/a[@data-name="Оргтехника и расходники"]'

    def __init__(self, page: Page) -> None:
        self.page = page

    @allure.step("Close popup window")
    def close_popup(self) -> None:
        self.page.locator(self.POPUP_CLOSE_BUTTON).click()

    @allure.step("Click 'All categories' button")
    def click_all_categories_btn(self) -> None:
        self.page.locator(self.ALL_CATEGORIES_BTN).click()

    @allure.step("Hover 'Electronics' category")
    def hover_category_electronics(self) -> None:
        self.page.locator(self.CATEGORY_ELECTRONICS).hover()

    @allure.step("Click 'Orgtechnics and supplies' category")
    def click_category_orgtechnics_and_supplies(self) -> None:
        self.page.locator(self.CATEGORY_ORGTECHNICS_AND_SUPPLIES).click()

    @allure.step("Go to 'Orgtechnics and supplies' page")
    def goto_orgtechnics_and_supplies_page(self) -> OrgtechnicsAndSuppliesPage:
        self.close_popup()
        self.click_all_categories_btn()
        self.hover_category_electronics()
        self.click_category_orgtechnics_and_supplies()
        return OrgtechnicsAndSuppliesPage(self.page)
