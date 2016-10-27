from beedriver.po.elements.button import Button
from beedriver.po.elements.text_input import TextInput
from beedriver.po.page_object import PageObject
from .locators import SendMessageFormLocators as Locators


class SendMessageForm(PageObject):
    def init_child_objects(self):
        self.message_input = TextInput(self, Locators.MESSAGE_INPUT)
        self.submit_button = Button(self, Locators.SUBMIT_BUTTON)
