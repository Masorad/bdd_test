from beedriver.po.page_object import PageObject
from beedriver.po.widgets.tracy import Tracy
from beedriver.po.widgets.tracy.locators import TracyLocators
from .left_panel import LeftPanel
from .locators import EngagerLocators
from .login_page import LoginPage


class Engager(PageObject):
    def init_child_objects(self):
        self.login_page = LoginPage(self, EngagerLocators.LOGIN_PAGE)
        self.left_panel = LeftPanel(self, EngagerLocators.LEFT_PANEL)
        # self.care = Care(self, EngagerLocators.CARE)
        self.tracy = Tracy(self, TracyLocators.WRAPPER)

    def load(self):
        self.client.get(self.client.config.engager_url)
