from selenium.webdriver.remote.webelement import WebElement

from beedriver.po.page_object import PageObject


class InfoPanel(PageObject):
    def get_info_text(self):
        self.wait_for_exist()
        element = self.find()  # type: WebElement
        message_element = element.find_element_by_tag_name('span')  # type: WebElement

        return message_element.text
