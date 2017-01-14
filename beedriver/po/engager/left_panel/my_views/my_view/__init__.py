from beedriver.po.elements.button import Button
from selenium.common.exceptions import NoSuchElementException


class MyView(Button):

    def is_active(self):

        view = self.find()
        class_attribute = view.get_attribute('class')

        return 'active' in class_attribute
