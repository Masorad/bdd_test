from beedriver.po.elements.button import Button
from beedriver.po.elements.text_input import TextInput
from beedriver.po.page_object import PageObject
from .locators import LoginFormLocators as Locators


class LoginForm(PageObject):
    def init_child_objects(self):
        self.email = TextInput(self, Locators.EMAIL)
        self.password = TextInput(self, Locators.PASSWORD)
        self.submit_button = Button(self, Locators.BUTTON)
