from beedriver.po.page_object import PageObject
from .locators import LoginPageLocators
from .login_form import LoginForm

class LoginPage(PageObject):

    def init_child_objects(self):
        self.login_form = LoginForm(self, LoginPageLocators.LOGIN_FORM)

