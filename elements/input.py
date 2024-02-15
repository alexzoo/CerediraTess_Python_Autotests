from playwright.sync_api import Locator
from elements._base_element import BaseElement


class Input(BaseElement):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)
