from beedriver.po.page_object import PageObject
from .livechat_button import LiveChatButton
from .locators import LeftPanelLocators as Locators


class LeftPanel(PageObject):
    def init_child_objects(self):
        self.livechat_button = LiveChatButton(self, Locators.LIVECHAT_BUTTON)
