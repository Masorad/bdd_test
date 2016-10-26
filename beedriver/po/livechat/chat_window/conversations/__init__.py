from beedriver.po.page_object import PageObject
from .locators import ConversationsLocator


class Conversations(PageObject):
    def get_last_message(self):
        conversation_box = self.find()
        message_elements = conversation_box.find_elements_by_class_name(ConversationsLocator.MESSAGE_CONTENT_CLASS)

        return message_elements[-1].text
