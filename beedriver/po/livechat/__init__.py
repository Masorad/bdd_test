from beedriver.po.page_object import PageObject
from .chat_window import ChatWindow
from .locators import LiveChatLocators


class LiveChat(PageObject):
    def init_child_objects(self):
        self.chat_window = ChatWindow(self, LiveChatLocators.CHAT_WINDOW)

    def load(self):
        self.client.get(self.client.config.livechat_url)
