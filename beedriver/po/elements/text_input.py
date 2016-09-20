from beedriver.po.page_object import PageObject


class TextInput(PageObject):
    def clear(self):
        self.find().clear()
        return self

    def append(self, value):
        self.find().send_keys(value)
        return self

    def set(self, value):
        elem = self.find()
        elem.clear()
        elem.send_keys(value)
        return self
