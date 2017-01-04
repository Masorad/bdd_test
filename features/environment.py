import sys

sys.path.append('../')
from beedriver import get_beedriver

BEHAVE_DEBUG_ON_ERROR = False

def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")

def before_all(context):
    setup_debug_on_error(context.config.userdata)
    context.BeeDriver = get_beedriver

def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        # -- ENTER DEBUGGER: Zoom in on failure location.
        # NOTE: Use IPython debugger, same for pdb (basic python debugger).
        import ipdb
        ipdb.post_mortem(step.exc_traceback)


def before_scenario(context, scenario):
    context.browsers = dict()
    browsers_names = ['engager', 'office', 'livechat', 'switcher']
    for browser_name in browsers_names:
        context.browsers[browser_name] = dict()


def after_scenario(context, scenario):
    for browser_name in context.browsers.keys():
        for browser_index in context.browsers[browser_name].keys():
            if scenario.status == 'failed':
                screenshot_name = browser_name + '-' + browser_index + '-' + scenario.name.replace(' ', '_')
                context.browsers[browser_name][browser_index].save_screenshot('screenshots/' + screenshot_name + '.png')

            context.browsers[browser_name][browser_index].quit()

    del context.browsers
