from beedriver.po.elements.button import Button
from beedriver.po.elements.text_input import TextInput
from beedriver.po.page_object import PageObject
from .locators import StartChatFormLocators as Locators


class StartChatForm(PageObject):
    def init_child_objects(self):
        self.name = TextInput(self, Locators.NAME)
        self.submit_button = Button(self, Locators.BUTTON)
