from playwright.sync_api import Locator
from ._base_element import BaseElement


class Button(BaseElement):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)
