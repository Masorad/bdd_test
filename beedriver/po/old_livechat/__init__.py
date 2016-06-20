from beedriver.po.page_object import PageObject
from .locators import OldLiveChatLocators as Locators
from .chat_window import ChatWindow

class OldLiveChat(PageObject):

    def init_child_objects(self):
        self.chat_window = ChatWindow(self, Locators.CHAT_WINDOW)

    def load(self):
        self.client.get(self.client.config.old_livechat_url)
        window = self.chat_window
        window.wait_for_exist()
        iframe_element = window.find()
        self.client.switch_to_frame(iframe_element)

