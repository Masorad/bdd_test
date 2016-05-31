from .engager import EngagerAC
from .action_chain import ActionChain

class RootActionChain:

    def __init__(self, client):
        self.parent = None
        self.client = client
        self.engager = EngagerAC(self)

