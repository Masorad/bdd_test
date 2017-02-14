from beedriver.po.elements.button import Button
from beedriver.po.elements.text_input import TextInput
from beedriver.po.livechat.chat_window.agent_profile import AgentProfile
from beedriver.po.livechat.chat_window.info_panel import InfoPanel
from beedriver.po.livechat.chat_window.info_panel.locators import InfoPanelLocator
from beedriver.po.page_object import PageObject
from .agent_profile import AgentProfile
from .agent_profile.locators import AgentProfileLocator
from .conversations import Conversations
from .header import Header
from .header.locators import HeaderLocators
from .locators import ChatWindowLocators as Locators
from .offline_form import OfflineForm
from .send_message_form import SendMessageForm
from .start_chat_form import StartChatForm


class ChatWindow(PageObject):
    def init_child_objects(self):
        self.offline_form = OfflineForm(self, Locators.OFFLINE_FORM)
        self.start_chat_form = StartChatForm(self, Locators.START_CHAT_FORM)
        self.agent_profile = AgentProfile(
            self, AgentProfileLocator.AGENT_PROFILE
        )
        self.info_panel = InfoPanel(self, InfoPanelLocator.INFO)
        self.conversation = Conversations(self, Locators.CONVERSATION)
        self.send_message_form = SendMessageForm(self, Locators.REPLY_BOX)
        self.header = Header(self, HeaderLocators.HEADER)
        self.end_chat_message = PageObject(self, Locators.END_CHAT_BOX)
        self.settings_expander = Button(
            self, Locators.SETTINGS_EXPANDER
        )
        self.end_chat = Button(
            self, Locators.END_CHAT
        )
        self.send_transcript_icon = Button(
            self, Locators.SEND_TRANSCRIPT_ICON
        )
        self.send_transcript_link = Button(
            self, Locators.SEND_TRANSCRIPT_LINK
        )
        self.send_transcript_email_input = TextInput(
            self, Locators.SEND_TRANSCRIPT_EMAIL_INPUT
        )
        self.send_transcript_email_send_button = Button(
            self, Locators.SEND_TRANSCRIPT_EMAIL_SEND_BUTTON
        )
        self.send_transcript_close_button = Button(
            self, Locators.SEND_TRANSCRIPT_CLOSE_BUTTON
        )
        self.transcript_sent_success = PageObject(
            self, Locators.TRANSCRIPT_SENT_SUCCESS
        )

    def is_online(self):
        online_icon_element = self.base_xpath + Locators.STATUS_ELEMENT_ONLINE
        offline_icon_element = self.base_xpath \
            + Locators.STATUS_ELEMENT_OFFLINE

        if self.client.is_existing(online_icon_element):
            return True

        if self.client.is_existing(offline_icon_element):
            return False

        return self.header.is_existing() \
            and 'ONLINE' in self.header.find().get_attribute('data-status')

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
