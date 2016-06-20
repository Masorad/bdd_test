from beedriver.po.page_object import PageObject
from .locators import OfficeLocators
from .login_page import LoginPage
from .features import Features
from beedriver.po.widgets.tracy import Tracy
from beedriver.po.widgets.tracy.locators import TracyLocators

class Office(PageObject):

    def init_child_objects(self):
        self.login_page = LoginPage(self, OfficeLocators.LOGIN_PAGE)
        self.features = Features(self, OfficeLocators.FEATURES)
        self.tracy = Tracy(self, TracyLocators.WRAPPER)

    def load(self):
        self.client.get(self.client.config.office['url'])

