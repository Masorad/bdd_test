import os
import sys

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

sys.path.append('../')
from beedriver import get_beedriver_class

def before_all(context):
    # determine browser
    allowed_browsers = ['firefox', 'chrome']
    browser = os.getenv('BEEDRIVER_BROWSER')
    if not browser in allowed_browsers:
        browser = allowed_browsers[0]

    # get BeeDriver class and browser config
    if browser == 'chrome':
        base = webdriver.Remote
        context.browser_config = {
            'command_executor': 'http://127.0.0.1:4444/wd/hub',
            'desired_capabilities': DesiredCapabilities.CHROME
        }
    elif browser == 'firefox':
        base = webdriver.Firefox
        context.browser_config = dict()
    context.BeeDriver = get_beedriver_class(base)


def after_scenario(context, scenario):
    try: context.livechat_browser.quit()
    except: pass

    try: context.switcher_browser.quit()
    except: pass

