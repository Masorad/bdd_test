from beedriver.po.elements.button import Button
from beedriver.po.elements.text_input import TextInput
from beedriver.po.engager.livechat_settings.basic.locators import BasicLocators
from beedriver.po.page_object import PageObject


class Basic(PageObject):
    def init_child_objects(self):
        input_locator = '//*[@id="' + BasicLocators.maximum_sessions_per_agent_input_id + '"]'
        self.max_session_per_agent_input = TextInput(self, input_locator)
        self.sumbmit_button = Button(self, BasicLocators.submit_button)

    def load(self):
        self.client.get(self.client.config.engager_url + BasicLocators.url)

    def change_maximum_sessions_per_agent(self, number):
        if number == 'off':
            self.max_session_per_agent_input.set('')
            self.max_session_per_agent_input.disable()
        else:
            self.max_session_per_agent_input.enable()
            self.max_session_per_agent_input.set(number)
        self.sumbmit_button.makeVisible()
        self.sumbmit_button.click()
