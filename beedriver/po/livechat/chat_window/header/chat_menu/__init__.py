from beedriver.po.elements.button import Button
from beedriver.po.page_object import PageObject
from .locators import ChatMenuLocator as Locators


class ChatMenu(PageObject):
    def init_child_objects(self):
        self.close_chat_menu_item = Button(self, Locators.CHAT_MENU_CLOSE_ITEM)
