from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

base_class = webdriver.Remote
config = {
    'command_executor': 'http://seleniumhub:4444/wd/hub',
    'desired_capabilities': DesiredCapabilities.CHROME,
}
