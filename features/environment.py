import os
import sys

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

sys.path.append('../')
from beedriver import get_beedriver


def before_all(context):
    context.BeeDriver = get_beedriver

    context.browsers = dict()
    browsers = dict()
    browsers_names = ['engager', 'livechat', 'switcher']
    for browser_name in browsers_names:
        context.browsers[browser_name] = dict()


def after_scenario(context, scenario):
    for browser_name in context.browsers.keys():
        for browser_index in context.browsers[browser_name].keys():
            try: context.browsers[browser_name][browser_index].quit()
            except: pass

