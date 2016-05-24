from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from beedriver.po import RootPageObject

def get_beedriver_class(base=webdriver.Firefox):

    class BeeDriver(base):

        def start_client(self):
            self.po = RootPageObject(self)

        def is_existing(self, selector):
            try:
                elem = self.find_element_by_xpath(selector)
                return True
            except exceptions.NoSuchElementException:
                return False

        def wait_for_exist(self, selector, timeout=1):
            WebDriverWait(self, timeout).until(
                lambda x: self.is_existing(selector),
                message='Element "{}" not found after {} seconds.'.format(
                    selector, timeout)
            )

    return BeeDriver

