from beedriver.po.page_object import PageObject
from .locators import LiveChatLocators
from .chat_window import ChatWindow

class LiveChat(PageObject):

    def init_child_objects(self):
        self.chat_window = ChatWindow(self, LiveChatLocators.CHAT_WINDOW)

    def load(self):
        self.client.get(self.client.config.livechat_url)

