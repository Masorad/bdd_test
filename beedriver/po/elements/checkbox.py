from beedriver.po.elements.input import Input


class CheckBox(Input):
    def check(self):
        element = self.find()
        if not element.get_attribute('checked'):
            self.click()
