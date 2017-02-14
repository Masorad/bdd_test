from beedriver.po.page_object import PageObject


class Input(PageObject):
    def enable(self):
        self.client.execute_script(
            "arguments[0].removeAttribute('disabled');",
            self.find()
        )

    def makeVisible(self):
        self.client.execute_script(
            "arguments[0].style.display = 'block';",
            self.find()
        )

    def click(self):
        self.find().click()
        return self
