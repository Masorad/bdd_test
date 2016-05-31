from beedriver.po.page_object import PageObject
from .locators import LeftPanelLocators as Locators
from .livechat_button import LiveChatButton

class LeftPanel(PageObject):

    def init_child_objects(self):
        self.livechat_button = LiveChatButton(self, Locators.LIVECHAT_BUTTON)

