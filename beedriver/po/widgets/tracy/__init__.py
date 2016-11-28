from selenium.common.exceptions import TimeoutException

from beedriver.po.elements.button import Button
from beedriver.po.page_object import PageObject
from .locators import TracyLocators as Locators


class Tracy(PageObject):
    def init_child_objects(self):
        self.close_button = Button(self, Locators.CLOSE_BUTTON)

    def close(self):
        try:
            self.close_button.wait_for_exist()
        except TimeoutException:
            return  # We wait if tracy appears, if not lets move on.
        self.close_button.click()
