from beedriver.po.page_object import PageObject


class Button(PageObject):
    def click(self):
        self.find().click()
        return self

    def makeVisible(self):
        self.client.execute_script(
            "arguments[0].style.display = 'block';",
            self.find()
        )
