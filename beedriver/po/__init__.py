from .engager import Engager
from .livechat import LiveChat
from .office import Office
from .page_object import PageObject


class RootPageObject(PageObject):
    def __init__(self, client):
        # Intentionally no parent call here
        self.parent = None
        self.client = client
        self.base_xpath = ''
        self.engager = Engager(self, '')
        self.office = Office(self, '')
        self.livechat = LiveChat(self, '')
