from playwright.sync_api import Locator

from helpers.logger_helper import Logger, log_all_methods

logger = Logger.setup_logger(__name__)


@log_all_methods(logger)
class BaseElement(Locator):
    """
    This class is a base class for all page elements. It inherits from the Playwright Locator class.

    The @log_all_methods decorator is used to automatically log all methods of the class to the console.

    The __init__ method takes a Locator object as input and copies its properties to the BaseElement object.

    Parameters:
        locator (Locator): The Playwright Locator object that is used to locate the element on the page.

    Returns:
        None
    """
    def __init__(self, locator: Locator) -> None:
        # self.locator = locator
        self.__dict__.update(locator.__dict__)
