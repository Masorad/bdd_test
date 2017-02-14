from beedriver.po.page_object import PageObject
from beedriver.po.engager.livechat_settings.basic import Basic


class LiveChatSettings(PageObject):
    def init_child_objects(self):
        self.basic = Basic(self, '')
