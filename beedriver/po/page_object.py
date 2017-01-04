class PageObject:
    def __init__(self, parent, base_xpath, dont_chain_xpath=False):
        self.parent = parent
        self.client = self.parent.client
        if dont_chain_xpath:
            self.base_xpath = base_xpath
        else:
            self.base_xpath = self.parent.base_xpath + base_xpath
        self.init_child_objects()

    def init_child_objects(self):
        pass

    def find(self):
        return self.client.find_element_by_xpath(self.base_xpath)

    def is_existing(self):
        return self.client.is_existing(self.base_xpath)

    def wait_for_exist(self):
        self.client.wait_for_exist(self.base_xpath)

    def move_to(self):
        self.client.move_to(self.base_xpath)
