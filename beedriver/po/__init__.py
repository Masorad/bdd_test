from .engager import Engager
from .office import Office
from .livechat import LiveChat
from .old_livechat import OldLiveChat
from .brand_status_switcher import BrandStatusSwitcher
from .page_object import PageObject

class RootPageObject(PageObject):

    def __init__(self, client):
        self.parent = None
        self.client = client
        self.base_xpath = ''
        self.engager = Engager(self, '')
        self.office = Office(self, '')
        self.livechat = LiveChat(self, '')
        self.old_livechat = OldLiveChat(self, '')
        self.brand_status_switcher = BrandStatusSwitcher(self, '')

