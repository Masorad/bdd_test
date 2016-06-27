import os
import importlib
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from beedriver.po import RootPageObject
from beedriver.ac import RootActionChain

def get_browser():
    browser = os.getenv('BEEDRIVER_BROWSER') or 'default'
    browser_config_file = 'beedriver.browser.{}'.format(browser)
    return importlib.import_module(browser_config_file)

def get_beedriver():

    browser = get_browser()

    class BeeDriver(browser.base_class):

        def start_client(self):
            self.config = self.get_config()
            self.po = RootPageObject(self)
            self.ac = RootActionChain(self)

        def get_config(self):
            config = os.getenv('BEEDRIVER_CONFIG') or 'default'
            config_file = 'beedriver.config.{}'.format(config)
            return importlib.import_module(config_file)

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

    return BeeDriver(**browser.config)

