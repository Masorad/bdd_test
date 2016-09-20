import sys

sys.path.append('../')
from beedriver import get_beedriver


def before_all(context):
    context.BeeDriver = get_beedriver


def before_scenario(context, scenario):
    context.browsers = dict()
    browsers_names = ['engager', 'office', 'livechat', 'switcher']
    for browser_name in browsers_names:
        context.browsers[browser_name] = dict()


def after_scenario(context, scenario):
    for browser_name in context.browsers.keys():
        for browser_index in context.browsers[browser_name].keys():
            try:
                context.browsers[browser_name][browser_index].quit()
            except:
                pass

    del context.browsers
