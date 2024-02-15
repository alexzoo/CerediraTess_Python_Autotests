from playwright.sync_api import Locator


class BaseElement(Locator):
    def __init__(self, locator: Locator):
        self.__dict__.update(locator.__dict__)

