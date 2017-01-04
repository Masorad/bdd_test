from beedriver.po.elements.button import Button
from beedriver.po.page_object import PageObject
from .locators import ReplyBoxLocators
from .send_message_form import SendMessageForm
from .send_message_form.locators import SendMessageFormLocators


class ReplyBox(PageObject):
    def init_child_objects(self):
        self.send_message_form = SendMessageForm(
            self, SendMessageFormLocators.BASE_CLASS
        )
        self.note_tab = Button(
            self, SendMessageFormLocators.NOTE_TAB_CLASS, True
        )
