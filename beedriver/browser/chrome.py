from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

base_class = webdriver.Remote
config = {
    'command_executor': 'http://127.0.0.1:4444/wd/hub',
    'desired_capabilities': DesiredCapabilities.CHROME
}
