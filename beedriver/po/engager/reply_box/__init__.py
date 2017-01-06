from beedriver.po.elements.button import Button
from beedriver.po.elements.text_input import TextInput
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

        self.send_chat_link = Button(self, SendMessageFormLocators.SEND_TRANSCRIPT, True)
        self.send_email_link = Button(self, SendMessageFormLocators.SEND_TRANSCRIPT_EMAIL_BUTTON, True)
        self.email_input = TextInput(self, SendMessageFormLocators.EMAIL_INPUT)

    def has_sent_transcript_sucessfully(self):
        locator = self.base_xpath + SendMessageFormLocators.TRANSCRIPT_SEND_SUCCESS
        self.client.wait_for_exist(locator)
        return self.client.is_existing(locator)
