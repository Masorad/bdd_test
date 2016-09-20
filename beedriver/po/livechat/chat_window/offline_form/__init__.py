from beedriver.po.elements.button import Button
from beedriver.po.elements.text_input import TextInput
from beedriver.po.page_object import PageObject
from .locators import OfflineFormLocators as Locators


class OfflineForm(PageObject):
    def init_child_objects(self):
        self.name = TextInput(self, Locators.NAME)
        self.email = TextInput(self, Locators.EMAIL)
        self.message = TextInput(self, Locators.MESSAGE)
        self.submit_button = Button(self, Locators.BUTTON)
