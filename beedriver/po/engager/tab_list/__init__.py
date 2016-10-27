from beedriver.po.page_object import PageObject
from .locators import TabListLocators


class TabList(PageObject):
    def has_tab_with_title(self, title):
        tab_list = self.find()
        tabs = tab_list.find_elements_by_tag_name('a')
        for tab in tabs:
            if tab.text == title:
                return True

        return False

    def open_incomming_message(self):
        tab_list = self.find()
        tab_list.find_element_by_class_name(TabListLocators.INCOMING_MESSAGE_TAB_CLASS).click()
