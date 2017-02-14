from beedriver.po.page_object import PageObject


class InfoPanel(PageObject):
    def is_customer_in_queue_at(self, number):
        self.wait_for_exist()
        element = self.find()
        print('---')
        print(element.find_by_xpath('/div[1]/div[1]/b/span'))
        print('---')
        print('---')
