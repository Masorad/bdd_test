from beedriver.po.page_object import PageObject
from beedriver.po.elements.button import Button
from .locators import BrandStatusSwitcherLocators as Locators

class BrandStatusSwitcher(PageObject):

    def init_child_objects(self):
        self.online_button = Button(self, Locators.ONLINE_BUTTON)
        self.offline_button = Button(self, Locators.OFFLINE_BUTTON)

    def load(self):
        self.client.get('http://localhost:3000/?testing1234')

    def wait_for_status(self, status):
        self.client.wait_for_exist(Locators.label_by_status(status), 5)

