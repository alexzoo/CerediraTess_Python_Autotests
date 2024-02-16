from playwright.sync_api import Locator
from elements.base_element import BaseElement
from helpers.logger_helper import log_all_methods, Logger

logger = Logger.setup_logger(__name__)


@log_all_methods(logger)
class Input(BaseElement):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)
