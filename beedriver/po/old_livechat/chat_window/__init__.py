from beedriver.po.page_object import PageObject
from .locators import ChatWindowLocators as Locators

class ChatWindow(PageObject):

    def is_online(self):
        status_elem = self.client.find_element_by_xpath(Locators.STATUS)
        status_attribute = status_elem.get_attribute('class')
        return 'online' in status_attribute

