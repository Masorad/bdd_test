from beedriver.po.engager.livechat_settings import LiveChatSettings
from beedriver.po.engager.post_list import PostList
from beedriver.po.engager.post_list import PostListLocators
from beedriver.po.page_object import PageObject
from beedriver.po.widgets.tracy import Tracy
from beedriver.po.widgets.tracy.locators import TracyLocators
from .left_panel import LeftPanel
from .locators import EngagerLocators
from .login_page import LoginPage
from .post_tab import PostTab
from .post_tab.locators import PostTabLocators
from .reply_box import ReplyBox
from .reply_box.locators import ReplyBoxLocators
from .tab_list import TabList
from .tab_list.locators import TabListLocators


class Engager(PageObject):
    def init_child_objects(self):
        self.login_page = LoginPage(self, EngagerLocators.LOGIN_PAGE)
        self.left_panel = LeftPanel(self, EngagerLocators.LEFT_PANEL)
        self.tab_list = TabList(self, TabListLocators.TAB_LIST)
        self.post_list = PostList(self, PostListLocators.POST_LIST)
        self.post_tab = PostTab(self, PostTabLocators.POST_TAB_WORKSPACE)
        self.reply_box = ReplyBox(self, ReplyBoxLocators.REPLY_BOX)
        self.tracy = Tracy(self, TracyLocators.WRAPPER)
        self.livechat_settings = LiveChatSettings(self, '')

    def load(self):
        self.client.get(self.client.config.engager_url)
