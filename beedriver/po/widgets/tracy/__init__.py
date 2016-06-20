from beedriver.po.page_object import PageObject
from beedriver.po.elements.button import Button
from .locators import TracyLocators as Locators

class Tracy(PageObject):

    def init_child_objects(self):
        self.close_button = Button(self, Locators.CLOSE_BUTTON)

    def close(self):
        self.close_button.wait_for_exist()
        self.close_button.click()

