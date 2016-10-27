from beedriver.po.page_object import PageObject
from .locators import PostTabLocators


class PostTab(PageObject):
    def get_last_livechat_message(self):
        tab_workspace = self.find()
        message_elements = tab_workspace.find_elements_by_class_name(PostTabLocators.LIVE_CHAT_MESSAGE_CLASS)
        last_message = message_elements[-1]

        return last_message.find_element_by_class_name(PostTabLocators.LIVE_CHAT_MESSAGE_TEXT_CLASS).text
