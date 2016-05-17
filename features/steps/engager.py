from behave import given, when, then, step
from helpers import validate_step_input

@given('brand is {status} for chat')
def brand_is_status_for_chat(context, status):
    # init browser
    context.switcher_browser = context.BeeDriver(**context.browser_config)
    switcher = context.switcher_browser.po.brand_status_switcher
    switcher.load()

    # change status
    context.execute_steps(
        "When brand goes {} for chat".format(status))

@step('brand goes {status} for chat')
def brand_goes_status_for_chat(context, status):
    valid_statuses = {'offline', 'online'}
    validate_step_input(status, valid_statuses)

    switcher = context.switcher_browser.po.brand_status_switcher
    if status == 'online':
        status_button = switcher.online_button
    elif status == 'offline':
        status_button = switcher.offline_button
    status_button.click()

