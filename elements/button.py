from playwright.sync_api import Locator

from helpers.logger_helper import Logger, log_all_methods
from .base_element import BaseElement

logger = Logger.setup_logger(__name__)


@log_all_methods(logger)
class Button(BaseElement):
    def __init__(self, locator: Locator) -> None:
        super().__init__(locator)

