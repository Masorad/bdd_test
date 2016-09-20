from beedriver.po.elements.button import Button


class LiveChatButton(Button):
    def is_online(self):
        button = self.find()
        status_attribute = button.get_attribute('class')
        return 'online' in status_attribute
