class ActionChain:
    def __init__(self, parent):
        self.parent = parent
        self.client = self.parent.client
