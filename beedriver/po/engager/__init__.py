from beedriver.po.page_object import PageObject
from .locators import EngagerLocators
from .login_page import LoginPage
#from .care import Care

class Engager(PageObject):

    def init_child_objects(self):
        self.login_page = LoginPage(self, EngagerLocators.LOGIN_PAGE)
        #self.care = Care(self, EngagerLocators.CARE)

    def load(self):
        self.client.get(self.client.config.engager_url)

