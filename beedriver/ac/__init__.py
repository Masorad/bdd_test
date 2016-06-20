from .engager import EngagerAC
from .office import OfficeAC

class RootActionChain:

    def __init__(self, client):
        self.parent = None
        self.client = client
        self.engager = EngagerAC(self)
        self.office = OfficeAC(self)

