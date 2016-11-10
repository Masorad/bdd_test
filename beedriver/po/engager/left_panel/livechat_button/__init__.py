from beedriver.po.elements.button import Button


class LiveChatButton(Button):
    def is_online(self):
        self.wait_for_exist()
        button = self.find()
        status_attribute = button.get_attribute('class')

        if 'online' not in status_attribute and 'offline' not in status_attribute:
            raise Exception(
                "Engager live-chat button has not any of 'online' nor 'offline' classes. Classes: ["
                + ", ".join(status_attribute) + "]")

        return 'online' in status_attribute
