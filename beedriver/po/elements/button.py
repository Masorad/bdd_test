from beedriver.po.page_object import PageObject

class Button(PageObject):

    def click(self):
        self.find().click()
        return self

