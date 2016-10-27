from beedriver.po.elements.button import Button
from beedriver.po.elements.text_input import TextInput
from beedriver.po.page_object import PageObject
from .locators import SendMessageFormLocators


class SendMessageForm(PageObject):
    def init_child_objects(self):
        self.message_input = TextInput(self, SendMessageFormLocators.MESSAGE_INPUT, True)
        self.submit_button = Button(self, SendMessageFormLocators.SUBMIT_BUTTON, True)
