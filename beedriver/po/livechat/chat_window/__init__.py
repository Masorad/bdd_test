from beedriver.po.page_object import PageObject
from .locators import ChatWindowLocators as Locators
from .start_chat_form import StartChatForm

class ChatWindow(PageObject):

    def init_child_objects(self):
        self.start_chat_form = StartChatForm(self, Locators.START_CHAT_FORM)

    def is_online(self):
        status_elem = self.client.find_element_by_xpath(Locators.STATUS)
        cls = status_elem.get_attribute('class')
        
        # the way to learn status is dependent on the window size - WRONG
        if 'Tmp' in cls: # window is expanded
            if status_elem.text == 'online':
                return True
            else:
                return False
        else: # window is collapsed
            if 'online' in cls:
                return True
            else:
                return False

    def is_collapsed(self):
        locator = self.base_xpath + Locators.HEADER_COLLAPSED
        return self.client.is_existing(locator)

    def is_expanded(self):
        locator = self.base_xpath + Locators.HEADER_EXPANDED
        return self.client.is_existing(locator)

    def _resize(self, action):
        if action == 'expand':
            locator = Locators.HEADER_COLLAPSED
        elif action == 'collapse':
            locator = Locators.HEADER_EXPANDED
        else:
            raise ValueError
        locator = self.base_xpath + locator
        self.client.wait_for_exist(locator)
        elem = self.client.find_element_by_xpath(locator)
        elem.click()

    def expand(self):
        self._resize('expand')
        
    def collapse(self):
        self._resize('collapse')

