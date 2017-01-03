from beedriver.po.page_object import PageObject
from beedriver.po.elements.button import Button
from .locators import HeaderLocators
from .chat_menu import ChatMenu
from .chat_menu.locators import ChatMenuLocator


class Header(PageObject):

    def init_child_objects(self):
        self.chat_menu_toggle = Button(self, HeaderLocators.CHAT_MENU_TOGGLE)
        self.chat_menu = ChatMenu(self, ChatMenuLocator.CHAT_MENU)

    def toggle_chat_menu(self):
        self.chat_menu_toggle.click()

