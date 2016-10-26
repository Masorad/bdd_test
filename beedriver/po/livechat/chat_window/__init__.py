from beedriver.po.page_object import PageObject
from .conversations import Conversations
from .locators import ChatWindowLocators as Locators
from .offline_form import OfflineForm
from .send_message_form import SendMessageForm
from .start_chat_form import StartChatForm


class ChatWindow(PageObject):
    def init_child_objects(self):
        self.offline_form = OfflineForm(self, Locators.OFFLINE_FORM)
        self.start_chat_form = StartChatForm(self, Locators.START_CHAT_FORM)
        self.agent_profile = PageObject(self, Locators.AGENT_PROFILE)
        self.conversation = Conversations(self, Locators.CONVERSATION)
        self.send_message_form = SendMessageForm(self, Locators.REPLY_BOX)

    def is_online(self):
        online_icon_element = self.base_xpath + Locators.STATUS_ELEMENT_ONLINE
        begin_conversation_element = self.base_xpath + Locators.BEGIN_CONVERSATION_BUTTON
        return self.client.is_existing(online_icon_element) or self.client.is_existing(begin_conversation_element)

    def is_collapsed(self):
        locator = self.base_xpath + Locators.HEADER_COLLAPSED
        self.client.wait_for_exist(locator)
        return self.client.is_existing(locator)

    def is_expanded(self):
        locator = self.base_xpath + Locators.HEADER_EXPANDED
        return self.client.is_existing(locator)

    def _resize(self, action):
        if action == 'expand':
            locator = Locators.HEADER_COLLAPSED
        elif action == 'collapse':
            locator = Locators.HEADER_EXPANDED
        else:
            raise ValueError
        locator = self.base_xpath + locator
        self.client.wait_for_exist(locator)
        elem = self.client.find_element_by_xpath(locator)
        elem.click()

    def expand(self):
        self._resize('expand')

    def collapse(self):
        self._resize('collapse')
