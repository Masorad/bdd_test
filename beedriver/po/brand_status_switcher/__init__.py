from beedriver.po.elements.button import Button
from beedriver.po.page_object import PageObject
from .locators import BrandStatusSwitcherLocators as Locators


class BrandStatusSwitcher(PageObject):
    def init_child_objects(self):
        self.online_button = Button(self, Locators.ONLINE_BUTTON)
        self.offline_button = Button(self, Locators.OFFLINE_BUTTON)

    def load(self):
        self.client.get(self.client.config.brand_status_switcher_url)
